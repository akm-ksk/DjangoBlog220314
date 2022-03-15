from unicodedata import category
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Tag
from django.core.paginator import Paginator

# Create your views here.
class BlogTop(ListView):
  model = Post
  context_object_name = "posts"
  template_name = 'blog/top.html'
  paginate_by = 9



class BlogCategory(ListView):
  model = Post
  context_object_name = "posts"
  template_name = 'blog/top.html'
  paginate_by = 9

  def get_queryset(self):
    slug = self.kwargs['slug']
    self.category = get_object_or_404(Category, slug=slug)
    return super().get_queryset().filter(category=self.category)



class BlogTag(ListView):
  model = Post
  context_object_name = "posts"
  template_name = 'blog/top.html'
  paginate_by = 9

  def get_queryset(self):
    slug = self.kwargs['slug']
    self.tag = get_object_or_404(Tag, slug=slug)
    return super().get_queryset().filter(tag=self.tag)



class BlogDetail(DetailView):
  model = Post
  template_name = 'blog/detail.html'

  def get_object(self, queryset=None):
    post = super().get_object(queryset)

    if post.publish or self.request.user.is_authenticated:
      return post
    else:
      raise Http404


