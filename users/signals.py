from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from .models import Profile


def create_user_profile(sender, instance, created, admin=True, **kwargs):
    Profile.objects.get_or_create(user=instance)
post_save.connect(create_user_profile, sender=User)

def save_recently_viewed(sender, user, request, **kwargs):
    pass   
#user_logged_in.connect(save_recently_viewed)