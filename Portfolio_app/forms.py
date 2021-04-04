from django import forms
from .models import *

class BlogEditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']
