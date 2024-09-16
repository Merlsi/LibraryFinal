from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import *
from .models import *
from .utils import DataMixin
from django.utils import timezone as tz


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


class AuthorList(ListView):
    model = Author
    template_name = 'library/author_list.html'
    context_object_name = 'posts'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/CRUD/create_book.html'
    success_url = reverse_lazy('author')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'library/CRUD/edit_book.html'
    fields = '__all__'
    success_url = reverse_lazy('author')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'library/CRUD/delete_book.html'
    success_url = reverse_lazy('author')
    slug_field = 'id'
    slug_url_kwarg = 'id'


class PublisherList(ListView):
    model = Publisher
    template_name = 'library/publisher_list.html'
    context_object_name = 'posts'


class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'library/CRUD/create_book.html'
    success_url = reverse_lazy('publisher')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'library/CRUD/edit_book.html'
    fields = '__all__'
    success_url = reverse_lazy('publisher')


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'library/CRUD/delete_book.html'
    success_url = reverse_lazy('publisher')
    slug_field = 'id'
    slug_url_kwarg = 'id'


class ExampleListView(ListView):
    # model = Example
    template_name = 'library/example_list.html'
    context_object_name = 'examples'

    def get_queryset(self):
        book = self.kwargs['book']
        print(book)
        examples = Example.objects.filter(book=book)
        print(examples)
        return examples


class ExampleDetailView(DetailView):
    template_name = 'library/example-detail.html'
    context_object_name = 'example'
    model = Example


class BorrowCreateView(CreateView):
    model = BookBorrower
    fields = ['borrower']
    success_url = reverse_lazy('books')
    template_name = 'library/book_form.html'

    def form_valid(self, form):
        try:
            last_borrow = BookBorrower.objects.filter(borrower=form.instance.borrower).latest('end')
        except:
            last_borrow = None
        if form.instance.borrower.debt:
            form.add_error('borrower', 'The user has\'t paid the fine')

            return self.form_invalid(form)

        if last_borrow is not None and last_borrow.status:
            form.add_error('borrower', 'The user has already borrowed a book')

            return self.form_invalid(form)
        print(self.kwargs['example'])
        exemplar = Example.objects.get(id=self.kwargs['example'])
        exemplar.status = 0
        exemplar.save()

        form.instance.example = exemplar

        response = super().form_valid(form)
        return response


class BorrowerListView(ListView):
    model = Borrower
    template_name = 'library/borrower-list.html'
    context_object_name = 'borrowers'

    def get_queryset(self):
        queryset = super().get_queryset()

        for borrow in BookBorrower.objects.filter(status=1):
            borrow.calculate_fine()
        return queryset


class BorrowerCreateView(CreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = 'library/CRUD/create_book.html'
    success_url = reverse_lazy('books')

    def test_func(self):
        return self.request.user.has_perm('library.create_borrower')

    def form_valid(self, form):
        password = User.objects.make_random_password()

        user = form.save()
        # user.save()

        borrower = Borrower(user=user)
        borrower.save()

        response = super().form_valid(form)
        return response


class BorrowerDetailView(DetailView):
    model = Borrower
    template_name = 'library/borrower-detail.html'
    context_object_name = 'borrower'


def clear_fine(request, pk):
    borrower = Borrower.objects.get(borrower_id=pk)
    borrower.debt = 0
    borrower.save()

    return redirect('borrower_detail', pk=borrower.borrower_id)


def end_borrow(request, pk):
    borrower = Borrower.objects.get(borrower_id=pk)

    last_borrow = BookBorrower.objects.filter(borrower=borrower).latest('end')
    last_borrow.end = tz.now()
    last_borrow.status = 0
    last_borrow.save()

    return redirect('borrower_detail', pk=pk)


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'library/login.html'

    def get_success_url(self):
        return reverse_lazy('books')


class MyLogoutView(LogoutView):
    redirect_field_name = True
