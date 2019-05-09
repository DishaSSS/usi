from django.db import models

# Create your models here.

class User(models.Model):

	password = models.CharField(
			max_length = 20
		)
	regid = models.CharField(
			max_length = 10
	)
	passw = models.CharField(
			max_length = 64
	)
	mood_reg = models.CharField(
			max_length = 10
	)
	mood_passw = models.CharField(
			max_length = 64
	)
	username = models.CharField(
			max_length = 64
	)


	def __str__(self):
		return self.username+"  "+self.password
