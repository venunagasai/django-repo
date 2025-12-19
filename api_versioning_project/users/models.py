from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	age=models.IntegerField()
	is_active=models.BooleanField(default=True)

	def __str__(self):
		return self.name
