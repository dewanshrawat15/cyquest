from django import forms
from django.db import models
from django.utils import timezone
from .models import Question
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	# question = forms.IntegerField()
	# solved_date = models.DateTimeField(
		# default=timezone.now)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')

		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError(("This email address is already in use. Please supply a different email address."))
		return email

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question', 'answer')