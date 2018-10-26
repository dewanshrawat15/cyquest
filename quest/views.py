from django.shortcuts import render, redirect
# from django.http.request import request
from .models import user
from .forms import reg_func, login_func
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request, 'quest/home.html', {})

def welcome(request):
	return render(request, 'quest/welcome.html', {})

def register(request):
	if request.method == "POST":
		form = reg_func(request.POST)
		if form.is_valid():
			db = form.save(commit=False)
			db.save()
			return redirect('home')
	else:
		form = reg_func()
	return render(request, 'quest/register.html', {'form': form})

def verify(request, str_username, str_password):
	# print(user.objects.filter(username=str_username).exists())
	y = user.objects.filter(username=str_username).exists()
	if(y and y.password==str_password):
		datausername = user.objects.get(username=str_username)
		datapassword = user.objects.get(password=str_password)
		if datausername==datapassword:
			return redirect(request, 'welcome')

	else:
		messages.error(request, 'username or password not correct')
		return redirect('login')

def login(request):
	if request.method == "POST":
		form = login_func(request.POST)
		if form.is_valid():
			# tempuser = user()
			temp_username = request.POST.get("username", "")
			temp_password = request.POST.get("password", "")
			verify(request ,temp_username, temp_password)				

	else:
		form = login_func()
	return render(request, 'quest/login.html', {'form': form})

def logout(request):
	temp_username = None
	temp_password = None
	return redirect('home')