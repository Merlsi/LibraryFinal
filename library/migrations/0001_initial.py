# Generated by Django 4.2 on 2023-04-19 10:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("name", models.CharField(db_index=True, max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "profile_img",
                    models.ImageField(
                        blank=True, default="img.png", null=True, upload_to=""
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, max_length=500)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("FI", "Fiction"),
                            ("NF", "Non-fiction"),
                            ("RM", "Romance"),
                            ("SC", "Science"),
                            ("PR", "Poetry"),
                            ("CB", "Cookbooks"),
                            ("MS", "Mistery"),
                        ],
                        default="RM",
                        max_length=2,
                    ),
                ),
                (
                    "cover",
                    models.ImageField(
                        blank=True, default="img.png", null=True, upload_to=""
                    ),
                ),
                (
                    "author_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="library.author",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Borrower",
            fields=[
                (
                    "borrower_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("debt", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("name", models.CharField(db_index=True, max_length=100)),
                ("last_name", models.CharField(blank=True, max_length=100)),
                (
                    "profile_img",
                    models.ImageField(
                        blank=True, default="img.png", null=True, upload_to=""
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Example",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("code", models.CharField(max_length=20)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="library.book"
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="library.publisher",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookBorrower",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Example",
                    ),
                ),
                (
                    "borrower_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.borrower",
                    ),
                ),
                (
                    "example_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.example",
                    ),
                ),
            ],
        ),
    ]