from django.urls import path


from .views import index, create_author, update_author, delete_author

urlpatterns = [
    path('', index, name='home'),
    path('create_author/', create_author, name='create_author'),
    path('update_author/<int:user_id>/', update_author, name='update_author'),
    path('delete_author/<int:user_id>', delete_author, name='delete_author')
]