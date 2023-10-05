from django.urls import path

from .views import home, postsListView

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('list_posts/', postsListView.as_view(), name='list_posts')
]