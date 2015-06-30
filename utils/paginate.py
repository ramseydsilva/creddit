from django.conf import settings


def get_paginated(request, entries):
    try:
        page = int(request.GET.get("page", 1))
    except:
        page = 1
    
    return entries[(page-1)*settings.API_LIMIT_PER_PAGE:page*settings.API_LIMIT_PER_PAGE]