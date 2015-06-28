from django.conf import settings
from .models import Category

def site_settings(request):
    return {
        'SETTINGS': settings.SETTINGS
    }

def main(request):
    try:
        page = int(request.GET.get("page", 1))
    except:
        page = 1
    return {
        'categories': Category.objects.all(),
        'page': page
    }
