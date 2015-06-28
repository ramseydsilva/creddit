from django.core.urlresolvers import reverse

def get_breadcrumb(text, url='', active=False):
    return {
        'active': active,
        'url': url,
        'text': text
    }

def home_breadcrumbs(active=True):
    breadcrumbs = []
    breadcrumbs.append(get_breadcrumb("Home", url=reverse("home"), active=active))
    return breadcrumbs

def category_breadcrumbs(category, active=True):
    breadcrumbs = home_breadcrumbs()
    breadcrumbs.append(get_breadcrumb(category.title, category.get_absolute_url(), active=active))
    return breadcrumbs

def get_parent_breadcrumbs(post):
    breadcrumb = []
    if post.parent:
        breadcrumb.append(get_breadcrumb(post.parent, post.parent.get_absolute_url()))
        breadcrumb = get_parent_breadcrumbs(post.parent) + breadcrumb
        return breadcrumb
    return breadcrumb

def post_breadcrumbs(post, active=True):
    breadcrumbs = category_breadcrumbs(post.category, active=False)
    breadcrumbs = breadcrumbs + get_parent_breadcrumbs(post)
    breadcrumbs.append(get_breadcrumb(post, post.get_absolute_url(), active=active))
    return breadcrumbs

def post_credits_breadcrumbs(post, active=True):
    breadcrumbs = post_breadcrumbs(post)
    breadcrumbs.append(get_breadcrumb("Credits", reverse("credits", args=[post.category.slug, post.slug]), active=active))
    return breadcrumbs

def profile_breadcrumbs(user, active=True):
    breadcrumbs = home_breadcrumbs()
    breadcrumbs.append(get_breadcrumb(user.username, user.profile.get_absolute_url(), active=active))
    return breadcrumbs

def inbox_breadcrumbs(user, active=True):
    breadcrumbs = profile_breadcrumbs(user)
    breadcrumbs.append(get_breadcrumb("Inbox", reverse("users:inbox", args=[user.username]), active=active))
    return breadcrumbs

def unread_breadcrumbs(user, active=True):
    breadcrumbs = inbox_breadcrumbs(user)
    breadcrumbs.append(get_breadcrumb("Unread", reverse("users:unread", args=[user.username]), active=active))
    return breadcrumbs

def upvoted_breadcrumbs(user, active=True):
    breadcrumbs = profile_breadcrumbs(user)
    breadcrumbs.append(get_breadcrumb("Upvoted", reverse("users:upvoted", args=[user.username]), active=active))
    return breadcrumbs

def downvoted_breadcrumbs(user, active=True):
    breadcrumbs = profile_breadcrumbs(user)
    breadcrumbs.append(get_breadcrumb("Downvoted", reverse("users:downvoted", args=[user.username]), active=active))
    return breadcrumbs