from django.urls import path

from .views import home, postsListView, create_user, update_user

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('list_posts/', postsListView.as_view(), name='list_posts'),
    path('create_user/', create_user, name='create_user'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
]