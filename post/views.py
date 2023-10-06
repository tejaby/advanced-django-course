from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .models import Post, User

from .forms import UserForm


# Create your views here.

class home(TemplateView):
    template_name = 'index.html'

class UserListView(ListView):
    model = User
    template_name = 'post/list_user.html'
    queryset = User.objects.filter(state=True)

class UserCreateView(CreateView):
    model = User
    template_name = 'post/create_user.html'
    form_class = UserForm
    success_url = reverse_lazy('list_user')

class UserUpdateView(UpdateView):
    model = User
    template_name = 'post/create_user.html'
    form_class = UserForm
    success_url = reverse_lazy('list_user')

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('list_user')

    def post(self, request, pk, *args, **kwargs):
        object = User.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('list_user')

class SigninView(FormView):
    template_name = 'post/signin.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('list_user')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('list_user')
        return self.render_to_response(self.get_context_data(form=form, error='Username or password is incorrect'))
