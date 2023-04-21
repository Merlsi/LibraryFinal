from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import *
from .models import *
from .utils import DataMixin

posts = Book.objects.all()


# Create your views here.
def index(request):
    return render(request, 'library/base.html')


class BookList(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'posts'


class ShowPost(DetailView):
    model = Book
    template_name = 'library/single_book.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/CRUD/create_book.html'
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'library/CRUD/edit_book.html'
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/CRUD/delete_book.html'
    success_url = reverse_lazy('books')
    slug_field = 'id'
    slug_url_kwarg = 'id'


