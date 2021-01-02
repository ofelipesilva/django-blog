from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Post

# Create your views here.
class BlogPageView(ListView):
    model = Post
    template_name = 'blog/blog.html'


class PostPageView(DetailView):
    model = Post
    template_name = 'blog/post.html'


class AboutPageView(TemplateView):
    template_name = 'blog/about.html'


class ContactPageView(TemplateView):
    template_name = 'blog/contact.html'