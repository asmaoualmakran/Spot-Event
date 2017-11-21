from django.conf.urls import url
from django.contrib import admin

from SpotEventApp.controllers import user, event, venue, address


urlpatterns = [
    url(r'^user$', user.user_request),
    url(r'^user/(?P<user_id>[0-9]+)/address', user.create_user_address),
#    url(r'^venue$', venue.venue_request),
#    url(r'^venue/(?P<venue_id>[0-9]+)/address', venue.create_venue_address),
    url(r'^event$', event.event_request),
    url(r'^event/(?P<event_id>[0-9]+)$', event.event_request),
    url(r'^address',address.address_request),
    url(r'^address/(?P<address_id>[0-9]+)$',address.address_request)
]

#urlpatterns = [
#	url(r'^events$', event.event_root)
	

#]