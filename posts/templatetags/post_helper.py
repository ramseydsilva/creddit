from django import template
from posts.models import Credit

register = template.Library()

def is_subscribed(post, user):
    if user.is_anonymous():
        return False
    return post.subscribers.filter(username=user.username).exists()

def has_upvoted(post, user):
    return Credit.objects.filter(post=post, user=user, amount=1).exists()

def has_downvoted(post, user):
    return Credit.objects.filter(post=post, user=user, amount=-1).exists()

register.filter('is_subscribed', is_subscribed)
register.filter('has_upvoted', has_upvoted)
register.filter('has_downvoted', has_downvoted)