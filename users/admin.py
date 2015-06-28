from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'credit')

class InboxAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'read')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Inbox, InboxAdmin)