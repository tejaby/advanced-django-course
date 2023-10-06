from django.urls import path

from .views import home, UserListView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('list_user/', UserListView.as_view(), name='list_user'),
    # path('create_user/', create_user, name='create_user'),
    # path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('create_user', UserCreateView.as_view(), name='create_user'),
    path('update_user/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', UserDeleteView.as_view(), name='delete_user')
]