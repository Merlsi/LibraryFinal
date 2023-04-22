from django.urls import path
from . import views
from django.shortcuts import HttpResponse

urlpatterns = [
    path('', views.index),
    path('books/', views.BookList.as_view(), name='books'),
    path('book/<str:pk>/', views.ShowPost.as_view(), name='book'),
    path('create-book/', views.BookCreateView.as_view(), name='create-book'),
    path('edit-book/<str:pk>', views.AuthorUpdateView.as_view(), name='book_edit'),
    path('delete-book/<uuid:id>/', views.BookDeleteView.as_view(), name='book_delete'),
    path('authors/', views.AuthorList.as_view(), name="author"),
    path('create-author/', views.AuthorCreateView.as_view(), name='create_author'),
    path('author_edit/<str:pk>', views.AuthorUpdateView.as_view(), name='author_edit'),
    path('delete-author/<uuid:id>/', views.AuthorDeleteView.as_view(), name='author_delete'),
    path('create_publisher/', views.PublisherCreateView.as_view(), name='create_publisher'),
    path('publishers/', views.PublisherList.as_view(), name="publisher"),
    path('publisher_edit/<str:pk>', views.PublisherUpdateView.as_view(), name='publisher_edit'),
    path('delete-publisher/<uuid:id>/', views.PublisherDeleteView.as_view(), name='publisher_delete')

]
