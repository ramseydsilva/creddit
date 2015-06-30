from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from .models import *
from utils import redirect
from posts.models import Post
from utils.breadcrumbs import *
from utils.paginate import get_paginated


def login_view(request, message="", username=""):
    next = request.REQUEST.get('next', reverse('home'))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect(request)
        elif not user.is_active:
            message = "This user has been deactivated."
        else:
            message = "Incorrect username/password."
    context ={
        'message' : message,
        'next' : next,
        'username': username,
        'breadcrumbs': login_breadcrumbs(next=next)
    }
    return render_to_response("users/login.html", context, context_instance = RequestContext(request))

def register_view(request, message="", username="", email=""):
    next = request.REQUEST.get('next', reverse('home'))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if username and password:
            if User.objects.filter(username=username).exists():
                message = "That username is taken"
            else:
                user = User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect(request)
        else:
            message = "Both username nd password are required."
    context ={
        'message' : message,
        'next' : next,
        'username': username,
        'email': email,
        'breadcrumbs': register_breadcrumbs(next=next)
    }
    return render_to_response("users/register.html", context, context_instance = RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect(request)

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
