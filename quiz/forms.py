from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
	
	class Meta:
		model = Question
		fields = ('question', 'answer', 'points',)

class PlayForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = ['answer']