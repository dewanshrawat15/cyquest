from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
	# author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	question = models.CharField(max_length=200)
	answer = models.CharField(max_length=32)

	def publish(self):
		# self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.question