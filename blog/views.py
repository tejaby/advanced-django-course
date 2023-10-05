from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post
from .forms import AuthorForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'index.html', {'post': posts})

def create_author(request):
    if request.method == 'GET':
        return render(request, 'create_author.html', {'form': AuthorForm})
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    
