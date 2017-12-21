from django.conf.urls import include, url
from django.contrib import admin
from SpotEventApp.controllers import controller
from SpotEventApp.controllers import user, event, venue, address, review, spotifyAuth
from SpotEventApp import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^profile/(?P<pk>[0-9]+)$', views.profile, name="profile"),
    url(r'^event/(?P<pk>[0-9]+)$', views.event, name="event"),
    url(r'^ticketevent/(?P<pk>([a-z]|[0-9])+)$', views.ticketevent, name="ticketevent"),
    url(r'^browse$', views.browse, name="browse"),
    url(r'^spotlight$', views.spotlight, name="spotlight"),
    url(r'^addevent$', views.addevent, name="addevent"),
    url(r'^search/(?P<pk>([a-z]|[0-9])+)$', views.search, name="search"),
    url(r'^spotifyAuth$', spotifyAuth.login, name=None),
    url(r'^authed$', spotifyAuth.request_Auth, name=None),
    url(r'^refresh_token/(?P<pk>[0-9]+)$', spotifyAuth.refresh_token, name=None),
]

