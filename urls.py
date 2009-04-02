import os

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.date_based import archive_year
from django.conf import settings

admin.autodiscover()

from planeta.feeds import RssFeed, AtomFeed

feeds = {
    'rss': RssFeed,
    'atom': AtomFeed,
}

urlpatterns = patterns('',
    url(r'^admin/(.*)', admin.site.root),
    url(r'^post/$', 'planeta.views.post_list'),
    url(r'^post/(?P<object_id>\d+)/$', 'planeta.views.post', name='post'),
    url(r'^authors/$', 'planeta.views.authors_list', name='authors'),
    url(r'^$', 'planeta.views.post_list', name='home'),
    url(r'^page/(?P<page>[0-9]+)/$', 'planeta.views.post_list'),
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    url(r'^archives/?(?P<year>\d{4})?/?$', 'planeta.views.post_archive_year', name='archives'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}, name='media'),
        url(r'^gotchi/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, "gotchi")}),
    )
