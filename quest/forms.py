from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	# if email and User.objects.filter(email=email).exclude(username=username).exists():
 #            raise forms.ValidationError(u'Email addresses must be unique.')
 #        return email