from django.urls import path
from .views import NewsList, PostDetail, NewsSearch, CreatePost, EditPost, DeletePost


urlpatterns = [
   path('', NewsList.as_view(), name='home'),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', NewsSearch.as_view(), name='search'),
   path('create', CreatePost.as_view()),
   path('<int:pk>/edit', EditPost.as_view()),
   path('<int:pk>/delete', DeletePost.as_view()),
]