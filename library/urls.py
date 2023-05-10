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
    path('example-list/<str:book>', views.ExampleListView.as_view(), name='example_list'),
    path('example-detail/<str:pk>/', views.ExampleDetailView.as_view(), name='example_detail'),
    path('borrow-create/<str:example>/', views.BorrowCreateView.as_view(), name='borrow-create'),
    path('borrowers-list', views.BorrowerListView.as_view(), name='borrower-list'),
    path('borrower-create', views.BorrowerCreateView.as_view(), name='borrower-create'),
    path('borrower-detail/<str:pk>', views.BorrowerDetailView.as_view(), name='borrower_detail'),
    path('clear-fine/<str:pk>', views.clear_fine, name='clear_fine'),
    path('end-borrow/<str:pk>', views.end_borrow, name='end_borrow')
]



