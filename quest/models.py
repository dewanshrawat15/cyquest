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
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'question']
		question = 0

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')

		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError(("This email address is already in use. Please supply a different email address."))
		return email