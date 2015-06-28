from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Inbox(models.Model):
    post = models.ForeignKey("posts.Post")
    user = models.ForeignKey("auth.User", related_name="inbox")
    read = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'post'),)

class Profile(models.Model):
    user = models.OneToOneField(User)
    credit = models.IntegerField(default=0)
    
    class Meta:
        ordering = ("-credit",)
        
    def __unicode__(self):
        return "%s" % (self.user)

    def get_absolute_url(self):
        return "%s" % (reverse("users:profile", args=[self.user.username]))

    def give_credit(self, credit):
        self.credit += credit
        self.save()

    def compute_score(self):
        self.credit = 0
        for post in self.user.post_set.all():
            self.credit += post.credit

    def save(self, *args, **kwargs):
        self.compute_score()
        super(Profile, self).save(*args, **kwargs)


class Subscription(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey('posts.Post')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'post'),)

    def __unicode__(self):
        return "%s - %s" % (self.user, self.post)