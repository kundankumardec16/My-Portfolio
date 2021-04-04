from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm # UserCreationForm is inherited by UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('users:login')
		else:
			messages.warning(request, f'Username already taken or Password mismatch')
	else:
		form = UserRegisterForm()
	return render(request, 'registration/register.html', {'form': form})


