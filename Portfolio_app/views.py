from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from django.core.mail import send_mail
from Portfolio import settings
#from django.http import HttpResponse, HttpResponseNotFound

def homepage(request):
	context = {
		'Contributor': Post.objects.all()
	}
	return render(request, 'Homepage/home.html', context)

def blogs(request):
	obj = Post.objects.all().order_by('-date_posted')
	context = {'Posts': obj, 'Name': 'Welcome'}
	return render(request, 'Homepage/blogs.html', context)

def blog(request, post_id):
	obj = Post.objects.get(id=post_id)
	context = {'blog': obj}
	return render(request, 'blog/blog_inner.html', context)

@login_required
def edit_blog(request, post_id):
	post = Post.objects.get(id=post_id)
	if request.method == "POST":
		form = BlogEditForm(data=request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('blog', post_id=post_id)
	else:
		# No data submitted; create a blank form.
		form = BlogEditForm(instance=post)

	content = {'form': form, 'post': post}
	return render(request, 'blog/blog_inner_edit.html', content)

@login_required
def edit_delete_blog(request, post_id):
	post = Post.objects.get(id=post_id)
	if request.user == post.author:
		messages.success(request, f'"{post.title}" has been deleted')
		post.delete()
	else:
		messages.warning(request, f'Cannot delete someone else blog.')
	return redirect('blogs')

def resume(request):
	return render(request, 'resume/resume.html')

def contact(request):
	return render(request, 'contact/contact.html')

def sendmail(request):
	if request.method=="POST":
	     subject = request.POST['subject']
	     msg = 'Hi ' + request.POST['name'] + ',\n\n\n' + request.POST['message']
	     to = request.POST['email']
	     if User.objects.filter(username = request.POST['uname']).first():
	     	res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
	     	if(res == 1):
	     		messages.success(request, f'A copy of mail has been sent to "{to}"')
	     	else:
	     		messages.warning(request, f'Error encountered try again.')
	     return redirect('contact')
	else:
		return render(request,'contact/contact.html')

