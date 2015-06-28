from django.contrib import admin
from .models import *

class DefaultAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)

class PostAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "credit", "user", "created_date")
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, DefaultAdmin)
admin.site.register(Tag, DefaultAdmin)
admin.site.register(Credit, DefaultAdmin)
admin.site.register(Hit, DefaultAdmin)