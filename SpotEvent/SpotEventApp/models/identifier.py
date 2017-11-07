from django.db import models
from . import address


class Identifier(models.Model):
	address_id = models.ForeignKey(address.Address, null = True)


	def __str__(self):
		return '%s' % (self.id)

	class Meta:
		abstract = True
