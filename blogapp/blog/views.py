from django.views.generic import ListView
from django.shortcuts import render
from blog.models import Post

# Create your views here.
class BlogTop(ListView):
  model = Post
  context_object_name = "posts"