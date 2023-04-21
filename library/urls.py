from django.urls import path
from . import views
from django.shortcuts import HttpResponse

urlpatterns = [
    path('', views.index),
    path('books/', views.BookList.as_view(), name='books'),
    path('book/<str:pk>/', views.ShowPost.as_view(), name='book'),
    path('create-book/', views.BookCreateView.as_view(), name='create-book'),
    path('edit-book/<str:pk>', views.BookUpdateView.as_view(), name='book_edit'),
    path('delete-book/<uuid:id>/', views.BookDeleteView.as_view(), name='book_delete'),

]
