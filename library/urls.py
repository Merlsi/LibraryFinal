from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('books/', views.books, name='books'),
    path('book/<str:pk>/', views.book, name='book'),
    path('create-book/', views.createBook, name='create-book')
]