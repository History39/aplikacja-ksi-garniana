from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class BookMain(models.Model):
    title = models.TextField(max_length=400)
    author = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} {self.author}"

class BookDetail(models.Model):
    BOOK_COVER=[
        ("PAP", "Paperback"),
        ("HAR", "Hardcover"),
    ]

    publisher = models.TextField(max_length=300)
    publication_date = models.DateField()
    description = models.TextField()
    cover = models.CharField(max_length=3, choices=BOOK_COVER)
    price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.publication_date}"
class Book(models.Model):
    main = models.ForeignKey(BookMain, on_delete=models.CASCADE)
    detail = models.OneToOneField(BookDetail, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.main.title} {self.main.author}"
