from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question = models.TextField()
	answer = models.CharField(max_length=32, default=None)
	points = models.PositiveIntegerField(default=5)

	def publish(self):
		self.save()

	def __str__(self):
		return self.question

class Answer(models.Model):
	answer = models.CharField(max_length=32)

class stud(models.Model):
	name = models.CharField(max_length=32)
	username = models.CharField(max_length=32)
	points = models.PositiveIntegerField(default=0)
	lql = models.PositiveIntegerField(default=1)
	time = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.username

	def lqlpoints(self, score):
		self.points = self.points + score
		self.lql = self.lql + 1
		self.time = timezone.now()
		self.save()