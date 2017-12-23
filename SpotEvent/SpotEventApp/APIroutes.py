from django.conf.urls import url
from django.contrib import admin
from SpotEventApp.controllers import controller
from SpotEventApp.controllers import user, event, venue, address, review, spotifyAuth


urlpatterns = [
#ROOT-----------------------------------------------------------------------------------------
	url(r'^$', controller.api_root),
#USER-----------------------------------------------------------------------------------------
    url(r'^user$', user.user_request, name="user"),
    url(r'^user/(?P<pk>[0-9]+)$', user.single_user_request, name="user-detail"),
    url(r'^user/authenticate$',user.user_Authenticate),
    url(r'^user/logout$', user.user_logout),
#SPOTIFYAUTH----------------------------------------------------------------------------------
    url(r'^spotifyAuthed/(?P<pk>[0-9]+)$', spotifyAuth.single_spotifyAuth_request, name="spotifyAuth-detail"),
    url(r'^spotifyAuth$', spotifyAuth.login),
    url(r'^refresh_token/(?P<pk>[0-9]+)$', spotifyAuth.refresh_token),
#EVENT----------------------------------------------------------------------------------------
   	url(r'^event$', event.event_request, name="event"),
   	url(r'^event/(?P<pk>[0-9]+)$', event.single_event_request, name="event-detail"),
    url(r'^eventlike/(?P<pk>[0-9]+)/(?P<user_pk>[0-9])$', event.update_liked_list, name="event-detail"),
#ADDRESS--------------------------------------------------------------------------------------
    url(r'^address$',address.address_request, name="address"),
    url(r'^address/(?P<pk>[0-9]+)$',address.single_address_request, name="address-detail"),
#VENUE----------------------------------------------------------------------------------------
    url(r'^venue$',venue.venue_request, name="venue"),
    url(r'^venue/(?P<pk>[0-9]+)$',venue.single_venue_request, name="venue-detail"),
#REVIEW---------------------------------------------------------------------------------------
    url(r'^review$', review.review_request, name="review"),
    url(r'^review/(?P<pk>[0-9]+)$',review.single_review_request, name="review-detail"),
]

