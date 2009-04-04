# -*- coding: utf-8 -*-

from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import date_based, list_detail
from django.shortcuts import render_to_response

from models import Feed, Post

def post(request, *args, **kwargs):

    kwargs['queryset'] = Post.objects.filter(feed__is_active=True)
    kwargs['template_name'] = 'planeta/single_article.html'

    return list_detail.object_detail(request, *args, **kwargs)

def post_list(request, page=0, *args, **kwargs):
    kwargs['paginate_by'] = settings.PAGINATE_BY
    kwargs['page'] = page
    kwargs['queryset'] = Post.objects.filter(feed__is_active=True)

    return list_detail.object_list(request, *args, **kwargs)

def post_archive_year(request, year=None, *args, **kwargs):
    posts = Post.objects.filter(feed__is_active=True)

    kwargs['year'] = year is None and posts[0].date_modified.year or year
    kwargs['date_field'] = 'date_modified'
    kwargs['queryset'] = posts
    kwargs['make_object_list'] = True
    kwargs['allow_empty'] = True

    return date_based.archive_year(request, *args, **kwargs)

def author(request, *args, **kwargs):
    kwargs['queryset'] = Feed.objects.filter(id=kwargs['object_id'], is_active=True)
    kwargs['template_name'] = 'planeta/single_author.html'
    kwargs['extra_context'] = {'default_avatar': settings.MEDIA_URL + 'images/default.png'}

    return list_detail.object_detail(request, *args, **kwargs)

def authors_list(request, *args, **kwargs):
    kwargs['queryset'] = Feed.objects.filter(is_active=True)
    kwargs['template_name'] = 'planeta/author_list.html'
    kwargs['extra_context'] = {'default_avatar': settings.MEDIA_URL + 'images/default.png'}

    return list_detail.object_list(request, *args, **kwargs)
