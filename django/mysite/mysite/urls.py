from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admins-txe001/', include(admin.site.urls)),
                       url(r'^fitur-txe-001/', include('polls.urls')),
                       )
