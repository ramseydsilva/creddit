from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from users.models import Subscription, Inbox
from django.template import loader, Context
import itertools


post_full_template = loader.get_template("includes/post.html")
post_html_template = loader.get_template("includes/post_html.html")

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ("title",)
        
    def __unicode__(self):
        return "%s" % (self.title)
    
    def get_absolute_url(self):
        return reverse('category', args=[self.slug])
    
class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ("title",)
    
class Post(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category)
    thumb = ImageField(upload_to="thumbs", null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    credit = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children")
    first_parent = models.ForeignKey("self", null=True, blank=True, related_name="all_children")
    created_date = models.DateTimeField(auto_now_add=True)
    subscribers = models.ManyToManyField(User, through='users.Subscription', related_name='subscribed')
    edit_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ("-credit", "-created_date",)
        
    def __unicode__(self):
        return "%s" % (self.title if self.title else self.text[:20])

    def html(self, user=None):
        return post_html_template.render({
            'post': self,
            'user': user
        })

    def full_html(self, user=None):
        return post_full_template.render({
            'post': self,
            'user': user
        })
    
    def get_first_parent(self):
        if self.parent:
            return self.parent.get_first_parent()
        return self
    
    def give_credit(self, credit):
        self.credit += credit
        self.save(compute_credit=False)
        
    def compute_credit(self, save=True):
        credits = self.credit_set.all()
        self.credit = 0
        if credits:
            self.credit = credits.aggregate(models.Sum("amount"))["amount__sum"]
        if save: self.save(compute_credit=False)
    
    def get_url(self):
        return self.url if self.url else self.get_absolute_url()
    
    def get_absolute_url(self):
        return reverse('post', args=[self.category.slug, self.slug])

    def clean(self):
        if self.parent == self:
            raise ValidationError("Circular relationship with parent")
        if not self.url and not self.text:
            raise ValidationError("Enter a url or description.")
    
    def get_unique_slug(self, to_slug):
        slug = slugify(to_slug)
        for x in itertools.count(1):
            if not Post.objects.filter(slug=slug).exists():
                break
            slug = '%s-%d' %(to_slug, x)
        return slug
    
    def save(self, compute_credit=True):
        if not self.id:
            parent = self.get_first_parent()
            self.category = parent.category
            try:
                self.first_parent = parent
            except ValueError:
                self.first_parent = None
                
            if not self.slug:
                self.slug = self.get_unique_slug(self.title or self.text[:50])
        if compute_credit:
            self.compute_credit(save=False)
        
        super(Post, self).save()
    
class Hit(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-created_date",)
            
    def __unicode__(self):
        return "%s - %s" % (self.user, self.post)
    
class CreditManager(models.Manager):
    def upvotes(self, *args, **kwargs):
        return self.get_queryset().filter(**kwargs).filter(amount=1)
    def downvotes(self, *args, **kwargs):
        return self.get_queryset().filter(**kwargs).filter(amount=-1)
    
class Credit(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, related_name="credit_set")
    amount = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    objects = CreditManager()
    
    class Meta:
        ordering = ("-created_date",)
        unique_together = (("user", "post"))
        
    def __unicode__(self):
        return "%s - %s - %s" % (self.user, self.post, self.credit)
    
    def credit(self, amount=1):
        self.post.give_credit(-self.amount+amount)
        if self.post.user:
            self.post.user.profile.give_credit(-self.amount+amount)
        self.amount = amount
        self.save()
    
    def accredit(self):
        self.credit()
    
    def discredit(self):
        self.credit(amount=-1)
    
    def save(self, *args, **kwargs):
        super(Credit, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.post.give_credit(-self.amount)
        if self.post.user:
            self.post.user.profile.give_credit(-self.amount)
        super(Credit, self).delete(*args, **kwargs)
    