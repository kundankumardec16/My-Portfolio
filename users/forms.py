from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): #inheriting from UserCreationForm
	first_name = forms.CharField(max_length=20, required=True)
	middle_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	dob = forms.DateField(required=True)
	email = forms.EmailField(required=True) # default arguement in EmailField is required=True 

	class Meta:
		model = User
		fields = ['username', 'first_name', 'middle_name', 'last_name', 'dob', 'email', 'password1', 'password2']