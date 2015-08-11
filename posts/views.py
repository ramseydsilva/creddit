from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from utils import redirect
from utils.breadcrumbs import *
from utils.paginate import get_paginated
from .models import *
from .forms import *


def home(request):
    posts = Post.objects.filter(parent__isnull=True)
    context = {
        'posts': get_paginated(request, posts),
        'breadcrumbs': home_breadcrumbs(),
    }
    return render_to_response("posts/home.html", context, context_instance = RequestContext(request))

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(parent__isnull=True, category=category)
    context = {
        'posts': get_paginated(request, posts),
        'category': category,
        'breadcrumbs': category_breadcrumbs(category),
    }
    return render_to_response("posts/category.html", context, context_instance = RequestContext(request))

@csrf_exempt
def post(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
    
    if request.POST:
        if request.user.is_anonymous():
            raise PermissionDenied # Redirect to login
        
        if request.POST["text"]:
            reply = Post(text=request.POST["text"], user=request.user, parent=post)
            reply.save()
            return redirect(request)
            
    context = {
        'post': post,
        'category': post.category,
        'breadcrumbs': post_breadcrumbs(post),
    }
    return render_to_response("posts/post.html", context, context_instance = RequestContext(request))

@csrf_exempt
def edit(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)

    if request.user.is_anonymous() or request.user != post.user:
        raise PermissionDenied # Redirect to login
        
    if request.POST:
        post.text = request.POST["text"]
        post.edit_count += 1
        post.save()
        return redirect(request)
            
    context = {
        'post': post,
        'category': post.category,
        'next': request.META['HTTP_REFERER'],
        'breadcrumbs': post_edit_breadcrumbs(post),
    }
    return render_to_response("posts/edit.html", context, context_instance = RequestContext(request))

@csrf_exempt
def delete(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)

    if request.user.is_anonymous() or request.user != post.user:
        raise PermissionDenied # Redirect to login
        
    if request.POST:
        if not post.children.all() and request.POST["make_anonymous"] == "0":
            post.delete()
        else:
            post.user = None
            post.save()
        return redirect(request)
            
    context = {
        'post': post,
        'category': post.category,
        'next': request.META['HTTP_REFERER'],
        'breadcrumbs': post_edit_breadcrumbs(post),
    }
    return render_to_response("posts/delete.html", context, context_instance = RequestContext(request))

def credits(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
    context = {
        'post': post,
        'category': post.category,
        'upvotes': Credit.objects.upvotes(post=post),
        'downvotes': Credit.objects.downvotes(post=post),
        'breadcrumbs': post_credits_breadcrumbs(post)
    }
    return render_to_response("posts/credits.html", context, context_instance = RequestContext(request))

@login_required
def upvote(request, category_slug, post_slug):
    print post_slug, category_slug
    post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
    credit, created = Credit.objects.get_or_create(user=request.user, post=post)
    if created:
        credit.accredit()
    else:
        if credit.amount < 0:
            credit.accredit()
        else:
            credit.delete()
    return redirect(request)

@login_required
def downvote(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
    credit, created = Credit.objects.get_or_create(user=request.user, post=post)
    if created:
        credit.discredit()
    else:
        if credit.amount > 0:
            credit.discredit()
        else:
            credit.delete()
    return redirect(request)

@login_required
def new(request, category_slug=None):
    category = Category.objects.filter(slug=category_slug).first()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(request, url=reverse("post", args=[post.category.slug, post.slug]))
    else:
        form = PostForm(initial={'category': category})
    context = {
        'form': form,
        'category': category
    }
    return render_to_response("posts/new.html", context, context_instance = RequestContext(request))

@login_required
def subscribe(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
    if not post.subscribers.filter(username=request.user.username).exists():
        Subscription(post=post, user=request.user).save()
    return redirect(request)

@login_required
def unsubscribe(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
    exists = Subscription.objects.filter(post=post, user=request.user).first()
    if exists:
        exists.delete()
    return redirect(request)