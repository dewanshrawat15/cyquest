from django import forms
from .models import user

# Register
class reg_func(forms.ModelForm):

	class Meta:
		model = user
		fields = ('name', 'email', 'username', 'password')

	def __init__(self, *args, **kwargs):
		super(reg_func, self).__init__(*args, **kwargs)
		self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter Password'})
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['placeholder'] = 'Enter Name'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
		self.fields['password'].widget.attrs['class'] = 'form-control'


# Login
class login_func(forms.ModelForm):

	class Meta:
		model = user
		fields = ('username', 'password')

	def __init__(self, *args, **kwargs):
		super(login_func, self).__init__(*args, **kwargs)
		self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter Password'})
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
		self.fields['password'].widget.attrs['class'] = 'form-control'