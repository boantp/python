from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admins/', include(admin.site.urls)),
                       url(r'^polls/', include('polls.urls')),
                       #url(r'^$', views.statusss),
                       )
