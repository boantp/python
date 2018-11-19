from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
                       #url(r'^bupati', 'polls.views.bupati', name='bupati'),
                       url(r'^$', views.index),
                       #/polls/2/
                       url(r'^(?P<poll_id>[0-9]+)/$', views.detail, name='detail'),
                       )
