from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

class User_Self(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	question = forms.IntegerField(
		widget=forms.HiddenInput(), initial=0)
	solved_date = models.DateTimeField(
		default=timezone.now)
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')

		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError(("This email address is already in use. Please supply a different email address."))
		return email


class Question(models.Model):
	# author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	question = models.CharField(max_length=200)
	answer = models.CharField(max_length=32)

	def publish(self):
		# self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.question