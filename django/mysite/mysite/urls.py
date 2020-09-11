from django.conf.urls import patterns, include, url
from django.contrib import admin
#test
urlpatterns = patterns('',
                       url(r'^admins/', include(admin.site.urls)),
                       url(r'^pollss/', include('polls.urls')),
                       #url(r'^$', views.status),
                       )
