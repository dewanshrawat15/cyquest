from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def home(request):
	return render(request, 'quest/home.html', {})

def welcome(request):
	return render(request, 'quest/welcome.html', {})

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			messages.success(request, f'Account created for { username }!')
			return redirect('welcome')

	else:
		form = UserRegisterForm()
	return render(request, 'quest/register.html', {'form': form})