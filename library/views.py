from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView

from .forms import *
from .models import *
from .utils import DataMixin

books = Book.objects.all()


# Create your views here.
def index(request):
    return render(request, 'library/base.html')


class BookList(DataMixin, ListView):
    model = Book
    template_name = 'library/book.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main Page")
        return context | c_def


def books(request):
    posts = Book.objects.all()
    return render(request, 'library/book.html', {'posts': posts})


def book(request, pk):
    return render(request, 'library/single_book.html')


def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    context = {'form': form}
    return render(request, "library/book_form.html", context)
