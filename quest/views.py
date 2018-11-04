from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .forms import UserRegisterForm, QuestionForm, EditProfile
from .models import Question, User_Self
# Create your views here.

def home(request):
	return render(request, 'quest/home.html', {})

def faq(request):
	return render(request, 'quest/faq.html', {})

@login_required
def profile(request):
	return render(request, 'quest/profile.html', {})

@login_required
def edit(request):
	if request.method == 'POST':
		form = EditProfile(request.POST, instance = request.user)
		if form.is_valid():
			user = form.save()
			return redirect('profile')
		else:
			messages.error(request, 'Please correct the following errors.')
	else:
		form = EditProfile(instance = request.user)
	return render(request, 'quest/edit.html', {'form': form})

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.POST, instance = request.user)
		if form.is_valid():
			user = form.save()
			return redirect('profile')

	else:
		form = PasswordChangeForm(instance = request.user)
	return render(request, 'quest/password_change.html.html', {'form': form})

def register(request):
	args = {}
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for { username }!')
			return redirect('profile')

	else:
		form = UserRegisterForm()
	args['form'] = form
	return render(request, 'quest/register.html', {'form': form}, args)

@login_required
@permission_required('quest.change_quest', raise_exception=True)
def question(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			Question = form.save(commit=False)
			Question.save()
			messages.success(request, f'Question Saved!')
			return redirect('question')

	else:
		form = QuestionForm()
	return render(request, 'quest/question.html', {'form': form})