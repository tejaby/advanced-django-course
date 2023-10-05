from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView

from .models import Post


# Create your views here.

class home(TemplateView):
    template_name = 'index.html'

class postsListView(ListView):
    model = Post
    template_name = 'post/list_post.html'
