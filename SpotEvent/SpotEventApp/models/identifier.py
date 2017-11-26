from django.db import models
from SpotEventApp.models.address import Address


#This table is used to avoid multiple null values in the 
#address table, this table wil only hold id's of the users and venues and id's of
#addresses

class Identifier(models.Model):
	address_id = models.ForeignKey(Address, related_name='address_id')



