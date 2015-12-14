__author__ = 'nicholassaunderson'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from Rhino import urls
from django.http import HttpResponseRedirect, HttpResponse

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('Rhino.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('Rhino.urls')),
)
