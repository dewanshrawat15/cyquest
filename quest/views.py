from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def home(request):
	return render(request, 'quest/home.html', {})

def welcome(request):
	return render(request, 'quest/welcome.html', {})

@login_required
def profile(request):
	return render(request, 'quest/profile.html', {})

def register(request):
	args = {}
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for { username }!')
			return redirect('welcome')

	else:
		form = UserRegisterForm()
	args['form'] = form
	return render(request, 'quest/register.html', {'form': form}, args)