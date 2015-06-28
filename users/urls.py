from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',

    url(r'^login/$', 'login_view', name='login'),
    url(r'^logout/$', 'logout_view', name='logout'),
    
    url(r'^u/(?P<username>[-\w]+)/$', 'profile', name='profile'),
    url(r'^u/(?P<username>[-\w]+)/inbox/$', 'inbox', name='inbox'),
    url(r'^u/(?P<username>[-\w]+)/inbox/unread/$', 'unread', name='unread'),
    url(r'^u/(?P<username>[-\w]+)/upvoted/$', 'upvoted', name='upvoted'),
    url(r'^u/(?P<username>[-\w]+)/downvoted/$', 'downvoted', name='downvoted'),
)