from django.conf import settings


def get_paginated(request, entries):
    try:
        page = int(request.GET.get("page", 1))
    except:
        page = 1
    entries = entries[(page-1)*settings.ITEMS_PER_PAGE:page*settings.ITEMS_PER_PAGE]
    return entries