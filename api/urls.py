from django.conf.urls import include, url
from api.resources import PostResource

post_resource = PostResource()

urlpatterns = [
    url(r'', include(post_resource.urls)),
]