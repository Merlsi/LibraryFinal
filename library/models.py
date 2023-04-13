from django.db import models
import uuid
import datetime


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    FICTION = 'FI'
    NON_FICTION = 'NF'
    ROMANCE = 'RM'
    SCIENCE = "SC"
    POETRY = "PR"
    COOKBOOKS = "CB"
    MISTERY = "MS"
    CATEGORIES = [
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-fiction'),
        (ROMANCE, 'Romance'),
        (SCIENCE, 'Science'),
        (POETRY, 'Poetry'),
        (COOKBOOKS, 'Cookbooks'),
        (MISTERY, 'Mistery')
    ]

    category = models.CharField(max_length=2, choices=CATEGORIES, default=ROMANCE)
    cover = models.ImageField(blank=True, null=True, default='img.png')
    author_id = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100)
    profile_img = models.ImageField(blank=True, null=True, default='img.png')

    def __str__(self):
        return self.name


class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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

    # duration = models.DurationField(datetime.now + datetime.timedelta(days=20, hours=10))

    def __str__(self):
        return str(self.id)
