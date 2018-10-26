from django.db import models
from django.utils import timezone

class user(models.Model):
	name = models.CharField(max_length=40)
	email = models.CharField(max_length=80)
	username = models.CharField(max_length=40)
	password = models.CharField(max_length=40)
	registered_date = models.DateTimeField(
			default=timezone.now)
	current_question = models.IntegerField(default=0)

	def publish(self):
		self.save()

	def __str__(self):
		return self.username