from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, ListView, UpdateView

from .models import Post, User

from .forms import UserForm


# Create your views here.

class home(TemplateView):
    template_name = 'index.html'

class postsListView(ListView):
    model = Post
    template_name = 'post/list_post.html'

def create_user(request):
    if request.method == 'POST':
        fomr_user = UserForm(request.POST)
        if fomr_user.is_valid():
            fomr_user.save()
        return redirect('home')
    else:
        return render(request, 'post/create_user.html', {'form': UserForm})
    
def update_user(request, user_id):
    try:
        user =get_object_or_404(User, id=user_id)
    except User.DoesNotExist:
        return HttpResponse("user not found", status=404)
    if request.method == 'POST':
        form_user = UserForm(request.POST, initial=user)
        if form_user.is_valid():
            form_user.save()
        return redirect('home')
    else:
        form = UserForm(instance=user)
        return render(request, 'post/create_user.html', {'form': form})