from django.urls import path, include
from . import views
#from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
	path('register/', views.register, name='register-form'),
	
	# Default login/logout way requires to create a registration directory containing login.html and logged_out.html
	path('', include('django.contrib.auth.urls')),

	# Only address to html file is required
	#path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]