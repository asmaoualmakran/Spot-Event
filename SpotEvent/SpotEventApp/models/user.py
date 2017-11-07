from django.db import models
from . import identifier

class User(identifier.Identifier):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	birthday = models.DateField()
	email = models.EmailField()

def __str__(self):
	return '%s (%s, %s)' % (self.id, self.first_name, self.last_name)


def calculate_age(self):
	import datetime 
	return int((datetime.date.today() - self.birthday).days / 356.25)

age = property(calculate_age)