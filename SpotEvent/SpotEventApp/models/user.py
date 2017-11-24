from django.db import models
from SpotEventApp.models.identifier import Identifier

class User(Identifier):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	birthday = models.DateField()
	email = models.EmailField()
	
# user doesn't need a field address, it inherits it  form
#identifier.

#def __str__(self):
#	return '%s (%s, %s)' % (self.id, self.first_name, self.last_name)


#def calculate_age(self):
#	import datetime 
#	return int((datetime.date.today() - self.birthday).days / 356.25)

#age = property(calculate_age)