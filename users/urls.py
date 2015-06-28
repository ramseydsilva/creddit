from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',
    url(r'^(?P<username>[-\w]+)/$', 'profile', name='profile'),
    url(r'^(?P<username>[-\w]+)/inbox/$', 'inbox', name='inbox'),
    url(r'^(?P<username>[-\w]+)/inbox/unread/$', 'unread', name='unread'),
    url(r'^(?P<username>[-\w]+)/upvoted/$', 'upvoted', name='upvoted'),
    url(r'^(?P<username>[-\w]+)/downvoted/$', 'downvoted', name='downvoted'),
)