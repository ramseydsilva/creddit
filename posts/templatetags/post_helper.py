from django import template
register = template.Library()

def is_subscribed(post, user):
    if user.is_anonymous():
        return False
    return post.subscribers.filter(username=user.username).exists()

register.filter('is_subscribed', is_subscribed)