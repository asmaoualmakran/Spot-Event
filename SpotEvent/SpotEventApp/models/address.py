from django.db import models


class Address(models.Model):
	street		= models.CharField(max_length=50)
	number		= models.CharField(max_length=5)
	zip_code	= models.CharField(max_length=10)
	city		= models.CharField(max_length=20)
	country		= models.CharField(max_length=20)

