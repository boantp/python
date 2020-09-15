from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admins/', include(admin.site.urls)),
                       url(r'^fitur/', include('polls.urls')),
                       )
