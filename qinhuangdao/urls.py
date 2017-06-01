#!/usr/bin/env python3

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<my_args>\d+)/$', views.detail, name='detail'),
    url(r'^draw/(?P<my_args>\d+)/$', views.draw, name='draw'),
    url(r'^show$',views.show, name='show')
]
