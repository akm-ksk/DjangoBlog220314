from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from blog.models import Post

# Create your views here.
class BlogTop(ListView):
  model = Post
  context_object_name = "posts"
  template_name = 'blog/top.html'



class BlogDetail(DetailView):
  model = Post
  template_name = 'blog/detail.html'

  def get_object(self, queryset=None):
    post = super().get_object(queryset)

    if post.publish or self.request.user.is_authenticated:
      return post
    else:
      raise Http404