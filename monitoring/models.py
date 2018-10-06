from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class data(models.Model):

	user = models.ForeignKey(User,on_delete=models.CASCADE,blank = True) 
	date = models.DateField(auto_now_add=True, blank=False)
	time = models.TimeField(auto_now_add=True, blank=False)
	moisture = models.DecimalField(default = 0.00, max_digits= 12, decimal_places=2)
	temperature = models.DecimalField(default = 0.00, max_digits= 12, decimal_places=2)

	def __str__(self):
		return '{}-{}'.format(self.date,self.time)