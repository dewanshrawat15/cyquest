from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Question, Answer, stud
from .forms import QuestionForm, PlayForm
# Create your views here.
@login_required
@permission_required('quest.change_quest', raise_exception=True)
def question(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			Question = form.save(commit=False)
			Question.save()
			return redirect('question')

	else:
		form = QuestionForm()
	return render(request, 'quiz/question.html', {'form': form})

def faq(request):
	return render(request, 'quiz/faq.html', {})

@login_required
def quiz(request):
	if request.method == 'POST':
		form = PlayForm(request.POST)
		if form.is_valid():
			answer = form.cleaned_data['answer']
			temp_username = request.user.username
			try:
				temp_stud = stud.objects.get(username=temp_username)
			except stud.DoesNotExist:
				temp_stud = False
			if not temp_stud:
				temp_user = User.objects.get(username=temp_username)
				stud.objects.create(name=temp_user.first_name, username=temp_username)
			
			temp_stud = stud.objects.get(username=temp_username)
			level = temp_stud.lql
			ans = Question.objects.get(pk=level)
			answ = ans.answer
			points = ans.points
			if answ == answer:
				temp_stud.lqlpoints(points)
	else:
		form = PlayForm()
	return render(request, 'quiz/question.html', {'form': form})