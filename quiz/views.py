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
			temp_stud = stud.objects.get(username=temp_username)
			level = temp_stud.lql
			ans = Question.objects.get(pk=level)
			answ = ans.answer
			points = ans.points
			if answ == answer:
				temp_stud.lqlpoints(points)
			form.save()
			obs = Answer.objects.all()
			obs.delete()
			return redirect(quiz)
	else:
		form = PlayForm()
	req = request.user.username
	try:
		temp_stud = stud.objects.get(username=req)
	except stud.DoesNotExist:
		temp_stud = False
	if not temp_stud:
		temp_user = User.objects.get(username=req)
		stud.objects.create(name=temp_user.first_name, username=req)
	temp_stud = stud.objects.get(username=req)
	try:
		lvl = temp_stud.lql
		ask = Question.objects.get(pk=lvl)
		return render(request, 'quiz/question.html', {'form': form, 'ask': ask})
	except:
		return render(request, 'quiz/result.html', {'points': temp_stud.points})

def leaderboard(request):
	stud_list = stud.objects.all().order_by('-points')
	return render(request, 'quiz/leaderboard.html', {'list': stud_list})