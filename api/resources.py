from tastypie.resources import ModelResource
from tastypie import fields
from posts.models import Post
from tastypie.authorization import Authorization
import copy


class PostResource(ModelResource):
    parent = fields.IntegerField(attribute="parent__id")
    user = fields.IntegerField(attribute="user__id")
    
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        include_resource_uri = True
        authorization = Authorization() # THIS IS IMPORTANT
        always_return_data = True
    
    def dehydrate(self, bundle):
        bundle.data['html'] = bundle.obj.html(user=bundle.request.user)
        return bundle
    
    def obj_create(self, bundle, **kwargs):
        bundle.data['user'] = bundle.request.user.id
        return super(PostResource, self).obj_create(bundle, user=bundle.request.user, parent_id=bundle.data['parent'])
    
    def get_object_list(self, request):

        if not request.user.is_anonymous() and request.GET.get("i"):
            first_parent = request.GET.get("fp")
            if first_parent:
                inbox = request.user.inbox.filter(read=False, post__first_parent=first_parent)
                unread = []
                for u in inbox:
                    unread.append(u.post.id)
                posts = Post.objects.filter(id__in=unread)
                for entry in inbox:
                    entry.read = True
                    entry.save()
                return posts
        return super(PostResource, self).get_object_list(request)
