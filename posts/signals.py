from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import Subscription, Inbox
from .models import Post

def subscription(sender, instance, created, raw, using, **kwargs):
    if created:
        # Subscribe user to his own post
        Subscription(post=instance, user=instance.user).save()

        # Send to inbox of people who suscribed to parent
        if instance.parent:
            for subscriber in instance.parent.subscribers.all():
                Inbox(post=instance, user=subscriber).save()

post_save.connect(subscription, sender=Post)