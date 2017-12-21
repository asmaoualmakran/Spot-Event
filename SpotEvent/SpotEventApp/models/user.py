from django.db import models
from SpotEventApp.models.identifier import Identifier
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password



#https://stackoverflow.com/questions/42075882/manager-object-has-no-attribute-get-by-natural-key
class UserAccountManager(BaseUserManager):
	def create_user(self, **kwargs):
		if not kwargs['email']:
			raise ValueError('Email must be set!')
		user = self.model(**kwargs)
		user.set_password(kwargs['password'])
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, last_name, password):
		user = self.create_user(email, first_name, last_name, password)
		user.is_admin = True
		user.save(using=self._db)
		return user

	def get_by_natural_key(self, email_):
		return self.get(email=email_)


class User(Identifier, AbstractUser):
	username 	= models.CharField(max_length=30, unique=True) # the username may contain alphanumeric, _, @, +, . and - characters
	first_name 	= models.CharField(max_length=30)
	last_name 	= models.CharField(max_length=30)
	birthday 	= models.DateField()
	email 		= models.EmailField(unique=True)

	objects = UserAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

#imageField