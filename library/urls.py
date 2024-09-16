import authentication as authentication
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.shortcuts import HttpResponse

urlpatterns = [
    path('', views.index),
    path('books/', views.BookList.as_view(), name='books'),
    path('book/<str:pk>/', views.ShowPost.as_view(), name='book'),
    path('create-book/', login_required(views.BookCreateView.as_view()), name='create-book'),
    path('edit-book/<str:pk>', login_required(views.AuthorUpdateView.as_view()), name='book_edit'),
    path('delete-book/<uuid:id>/', views.BookDeleteView.as_view(), name='book_delete'),
    path('authors/', views.AuthorList.as_view(), name="author"),
    path('create-author/', login_required(views.AuthorCreateView.as_view()), name='create_author'),
    path('author_edit/<str:pk>', login_required(views.AuthorUpdateView.as_view()), name='author_edit'),
    path('delete-author/<uuid:id>/', login_required(views.AuthorDeleteView.as_view()), name='author_delete'),
    path('create_publisher/', login_required(views.PublisherCreateView.as_view()), name='create_publisher'),
    path('publishers/', views.PublisherList.as_view(), name="publisher"),
    path('publisher_edit/<str:pk>', login_required(views.PublisherUpdateView.as_view()), name='publisher_edit'),
    path('delete-publisher/<uuid:id>/', login_required(views.PublisherDeleteView.as_view()), name='publisher_delete'),
    path('example-list/<str:book>', views.ExampleListView.as_view(), name='example_list'),
    path('example-detail/<str:pk>/', views.ExampleDetailView.as_view(), name='example_detail'),
    path('borrow-create/<str:example>/', login_required(views.BorrowCreateView.as_view()), name='borrow-create'),
    path('borrowers-list', login_required(views.BorrowerListView.as_view()), name='borrower-list'),
    path('borrower-create', login_required(views.BorrowerCreateView.as_view()), name='borrower-create'),
    path('borrower-detail/<str:pk>', login_required(views.BorrowerDetailView.as_view()), name='borrower_detail'),
    path('clear-fine/<str:pk>', login_required(views.clear_fine), name='clear_fine'),
    path('end-borrow/<str:pk>', login_required(views.end_borrow), name='end_borrow'),
    path('login', views.MyLoginView.as_view(),name='login'),
    path('logout', login_required(views.MyLogoutView.as_view()), name='logout'),

]
