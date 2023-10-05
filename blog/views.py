from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Author, Post
from .forms import AuthorForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'post': posts})

def create_author(request):
    if request.method == 'GET':
        return render(request, 'create_author.html', {'form': AuthorForm})
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
def update_author(request, user_id):
    author = Author.objects.get(id=user_id)
    if request.method == 'GET':
        form = AuthorForm(instance=author)
        return render(request, 'create_author.html', {'form': form})
    else:
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('home')


def delete_author(request, user_id):
    author = Author.objects.get(id=user_id)
    print(author)
    author.delete()
    return redirect('home')