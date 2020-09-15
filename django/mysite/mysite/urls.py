from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admins-txe001-undo-commit/', include(admin.site.urls)),
                       url(r'^fitur-txe-001-test/', include('polls.urls')),
                       )
