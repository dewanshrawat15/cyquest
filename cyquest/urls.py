"""cyquest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from quest import views as quest_view
from quiz import views as quiz_view

urlpatterns = [
	path('admin/', admin.site.urls),
	path('register/', quest_view.register, name='register'),
	path('faq/', quiz_view.faq, name='faq'),
	path('profile/edit/', quest_view.edit, name='edit'),
	path('login/', auth_views.LoginView.as_view(template_name='quest/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='quest/logout.html'), name='logout'),
	path('profile/', quest_view.profile, name='profile'),
	path('profile/password/', quest_view.change_password, name='change_password'),
	path('question/', quiz_view.question, name='question'),
	path('', quest_view.home, name='home'),
	path('quiz/', quiz_view.quiz, name='quiz'),
	path('leaderboard/', quiz_view.leaderboard, name='leaderboard'),
]
