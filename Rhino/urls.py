from django.conf.urls import patterns, include, url
from django.contrib import admin


from django.conf.urls import patterns, url
from Rhino import views
from django.http import HttpResponseRedirect, HttpResponse


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^home/', views.home, name='home'),
        )


