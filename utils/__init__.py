from django.shortcuts import redirect as django_redirect


def redirect(request, url=None):
    return django_redirect(url or request.GET.get("next") or request.POST.get("next") or request.META['HTTP_REFERER'])
