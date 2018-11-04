from django import forms
from django.db import models
from django.utils import timezone
from .models import Question, User_Self
from django.contrib.auth.models import User

class UserRegisterForm(User_Self):
	model = User

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question', 'answer')