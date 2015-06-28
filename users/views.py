from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from .models import *
from posts.models import Post
from utils.breadcrumbs import profile_breadcrumbs, inbox_breadcrumbs, unread_breadcrumbs, \
    upvoted_breadcrumbs, downvoted_breadcrumbs
from utils.paginate import get_paginated


def login(request):
    return render_to_response("users/login.html", context, context_instance = RequestContext(request))

def logout(request):
    return render_to_response("users/logout.html", context, context_instance = RequestContext(request))

def profile(request, username):
    this_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=this_user)
    context = {
        'this_user': this_user,
        'posts': get_paginated(request, posts),
        'breadcrumbs': profile_breadcrumbs(this_user)
    }
    return render_to_response("users/profile.html", context, context_instance = RequestContext(request))

@login_required
def inbox(request, username):
    this_user = get_object_or_404(User, username=username)
    
    if request.user != this_user: raise PermissionDenied
    
    inbox = request.user.inbox.all()
    posts = list(Post.objects.filter(id__in=inbox.values('post')))
    context = {
        'this_user': this_user,
        'posts': get_paginated(request, posts),
        'breadcrumbs': inbox_breadcrumbs(this_user)
    }
    return render_to_response("users/inbox.html", context, context_instance = RequestContext(request))

@login_required
def unread(request, username):
    this_user = get_object_or_404(User, username=username)
    
    if request.user != this_user: raise PermissionDenied
    
    inbox = request.user.inbox.filter(read=False)
    posts = list(Post.objects.filter(id__in=inbox.values('post')))
    for entry in inbox:
        entry.read = True
        entry.save()
    context = {
        'this_user': this_user,
        'posts': posts,
        'breadcrumbs': unread_breadcrumbs(this_user)
    }
    return render_to_response("users/inbox.html", context, context_instance = RequestContext(request))

def upvoted(request, username):
    this_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(id__in=this_user.credit_set.filter(amount=1).values('post'))
    context = {
        'this_user': this_user,
        'posts': get_paginated(request, posts),
        'breadcrumbs': upvoted_breadcrumbs(this_user)
    }
    return render_to_response("users/profile.html", context, context_instance = RequestContext(request))

def downvoted(request, username):
    this_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(id__in=this_user.credit_set.filter(amount=-1).values('post'))
    context = {
        'this_user': this_user,
        'posts': get_paginated(request, posts),
        'breadcrumbs': downvoted_breadcrumbs(this_user)
    }
    return render_to_response("users/profile.html", context, context_instance = RequestContext(request))
