from django.conf.urls import url
from django.contrib import admin
from SpotEventApp.controllers import controller
from SpotEventApp.controllers import user, event, venue, address, review


urlpatterns = [
	url(r'^$', controller.api_root),
    url(r'^user$', user.user_request, name="user"),
    url(r'^user/(?P<pk>[0-9]+)$', user.single_user_request, name="user-detail"),
   	url(r'^event$', event.event_request, name="event"),
   	url(r'^event/(?P<pk>[0-9]+)$', event.single_event_request, name="event-detail"),
    url(r'^address$',address.address_request, name="address"),
    url(r'^address/(?P<pk>[0-9]+)$',address.single_address_request, name="address-detail"),
    url(r'^venue$',venue.venue_request, name="venue"),
    url(r'^venue/(?P<pk>[0-9]+)$',venue.single_venue_request, name="venue-detail"),
    url(r'^review$', review.review_request, name="review"),
    url(r'^review/(?P<pk>[0-9]+)$',review.single_review_request, name="review-detail")
]

