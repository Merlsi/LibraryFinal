from django.db import models
import uuid
import datetime

from django.urls import reverse


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000, blank=True)
    FICTION = 'Fiction'
    NON_FICTION = 'Non-fiction'
    ROMANCE = 'Romance'
    SCIENCE = "Science"
    POETRY = "Poetry"
    COOKBOOKS = "Cookbook"
    MISTERY = "Mystery"
    CATEGORIES = [
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-fiction'),
        (ROMANCE, 'Romance'),
        (SCIENCE, 'Science'),
        (POETRY, 'Poetry'),
        (COOKBOOKS, 'Cookbooks'),
        (MISTERY, 'Mistery')
    ]

    category = models.CharField(max_length=20, choices=CATEGORIES, default=ROMANCE)
    cover = models.ImageField( blank=True, null=True, default='def.jpg')
    author_id = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_id': self.pk})


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100)
    profile_img = models.ImageField(blank=True, null=True, default='img.png')

    def __str__(self):
        return self.name


class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, blank=True)
    profile_img = models.ImageField(blank=True, null=True, default='img.png')

    def __str__(self):
        return self.name


class Example(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    publisher = models.ForeignKey("Publisher", on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=20)

    def __str__(self):
        return str(self.book)


class Borrower(models.Model):
    borrower_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    debt = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class BookBorrower(models.Model):
    id = models.UUIDField('Example', primary_key=True, default=uuid.uuid4, editable=False)
    example_id = models.ForeignKey("Example", on_delete=models.CASCADE)
    borrower_id = models.ForeignKey("Borrower", on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)
