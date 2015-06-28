from django.conf import settings
from django.conf.urls.static import static
from django.template.response import TemplateResponse
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # admin views
    url(r'^admin/', include(admin.site.urls)),
    url(r'u/', include('users.urls', namespace="users")),
    url(r'', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns +=  patterns('', (r'^404/$', TemplateResponse, {'template': '404.html'})) + \
                    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
                    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)