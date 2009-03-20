# -*- coding: utf-8 -*-

from models import Author
from django.conf import settings

def authors_list(request):
    return {
        'AUTHORS': Author.objects.all()
    }

def sansplanet_info(request):
    return {
        'PLANET_NAME': settings.PLANET_NAME,
        'PLANET_URL':settings.PLANET_URL
    }
