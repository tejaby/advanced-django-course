from django.urls import path


from .views import index, create_author

urlpatterns = [
    path('', index, name='home'),
    path('create_author/', create_author, name='create_author')
]