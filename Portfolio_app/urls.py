from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:post_id>', views.blog, name='blog'),
    path('blogs/edit/<int:post_id>', views.edit_blog, name='blog-edit'),
    path('blogs/edit/delete/<int:post_id>', views.edit_delete_blog, name='blog-edit-delete'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact')
]