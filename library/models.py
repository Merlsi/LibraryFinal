from django.db import models
import uuid
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


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
    cover = models.ImageField(blank=True, null=True, default='def.jpg')
    author = models.ManyToManyField('Author')

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
    STATUS_CHOICES = (
        (0, 'False'),
        (1, 'True'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    publisher = models.OneToOneField("Publisher", on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=20)
    print_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f"{Book.objects.get(id=self.book.id).title} - {self.code}"


def get_time():
    return timezone.now() + timedelta(seconds=50)


class Borrower(models.Model):
    borrower_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    debt = models.IntegerField(default=0)

    class Meta:
        ordering = ['borrower_id']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def has_exemplar(self):
        book = self.bookborrower_set.filter(status=1)

        if book:
            return book.first().exemplar

        return False


class BookBorrower(models.Model):
    STATUS_CHOICES = (
        (0, 'False'),
        (1, 'True'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    example = models.ForeignKey("Example", on_delete=models.CASCADE)
    borrower = models.ForeignKey("Borrower", on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    start = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True, default=get_time)

    def __str__(self):
        # instance = Example.objects.get(id=self.example.id)
        # borrower = Borrower.objects.get(id=self.borrower.borrower_id)
        return f'{self.example} {self.borrower}'
        # return f"{borrower.user.first_name} {borrower.user.last_name} - {instance}"

    def calculate_fine(self):
        time_now = timezone.now()
        print(f"Now: {time_now}")
        print(f"End: {self.end}")
        delta = (time_now - self.end)
        print(f"{self.borrower}: {delta}")
        if delta > timedelta(0):
            self.borrower.debt = delta.total_seconds()
            self.borrower.save()
