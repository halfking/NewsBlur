from django.conf.urls.defaults import *
from apps.rss_feeds import views

urlpatterns = patterns('',
    url(r'^feed_autocomplete', views.feed_autocomplete, name='feed-autocomplete'),
    url(r'^statistics/(?P<feed_id>\d+)', views.load_feed_statistics, name='feed-statistics'),
    url(r'^feed/(?P<feed_id>\d+)', views.load_single_feed, name='feed-info'),
    url(r'^exception_retry', views.exception_retry, name='exception-retry'),
    url(r'^exception_change_feed_address', views.exception_change_feed_address, name='exception-change-feed-address'),
    url(r'^exception_change_feed_link', views.exception_change_feed_link, name='exception-change-feed-link'),
    url(r'^status', views.status, name='status'),
    url(r'^load_single_feed', views.load_single_feed, name='feed-canonical'),
)
