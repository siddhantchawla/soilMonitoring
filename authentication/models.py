from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userprofile(models.Model): 

	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)

	
	def __str__(self):

		return '{}'.format(self.user)