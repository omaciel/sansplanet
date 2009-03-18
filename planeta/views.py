# -*- coding: utf-8 -*-

from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import date_based, list_detail
from django.shortcuts import render_to_response

from models import Post

def post_list(request, page=0):
    posts = Post.objects.all()

    return list_detail.object_list(
        request = request,
        queryset = Post.objects.all(),
        paginate_by = settings.PAGINATE_BY,
        page = page,
        #context_instance=RequestContext(request)
    )

def post_archive_year(request, year=None):
    posts = Post.objects.all()

    if not year:
        year = posts[0].date_modified.year

    return date_based.archive_year(
        request = request,
        year = year,
        date_field = 'date_modified',
        queryset = posts,
        make_object_list = True,
  )

def post(request, post_id):
    post = Post.objects.get(id=artigo_id)
    return render_to_response('planeta/post.html', locals())
