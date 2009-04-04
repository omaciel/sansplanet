# -*- coding: utf-8 -*-

from models import Post
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

def post_year_list(request):
    posts = Post.objects.filter(is_visible=True)

    years = []

    for post in posts:
        years.append(post.date_created.year)

    years = list(set(years))

    return {
        'ARCHIVES_YEAR_LIST': years,
    }
