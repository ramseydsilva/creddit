from django.conf.urls import patterns, url

urlpatterns = patterns('posts.views',
    url(r'^$', 'home', name='home'),
    url(r'^new/$', 'new', name='new'),
    url(r'^new/(?P<category_slug>[-\w]+)/$', 'new', name='new'),
    url(r'^(?P<category_slug>[-\w]+)/$', 'category', name='category'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[^/.]*)/$', 'post', name='post'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[^/.]*)/credits/$', 'credits', name='credits'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[^/.]*)/upvote/$', 'upvote', name='upvote'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[^/.]*)/downvote/$', 'downvote', name='downvote'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[^/.]*)/subscribe/$', 'subscribe', name='subscribe'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[^/.]*)/unsubscribe/$', 'unsubscribe', name='unsubscribe'),
)