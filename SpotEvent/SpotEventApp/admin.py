from django.contrib import admin
from SpotEventApp.models import user, review, identifier, venue, event, address

# Register your models here.
admin.site.register([user.User, review.Review, venue.Venue, event.Event, address.Address])