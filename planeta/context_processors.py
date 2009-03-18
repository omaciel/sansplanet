# -*- coding: utf-8 -*-

from django.conf import settings

def sansplanet_info(request):
    return {
        'PLANET_NAME': settings.PLANET_NAME,
        'PLANET_URL':settings.PLANET_URL
    }
