from django import forms
from django.db import models
from django.utils import timezone
from .models import User_Self
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(User_Self):
	model = User

	def update_details(self):
		password = self.cleaned_data.get('password1')
		firstname = self.cleaned_data.get('first_name')
		lastname = self.cleaned_data.get('last_name')

class EditProfile(UserChangeForm):

	class Meta:
		model = User
		fields = {'first_name', 'last_name', 'email'}