from django import forms
from .models import Book, BookDetail, BookMain
from django.forms import ModelForm, DateInput
from django.core.validators import MinValueValidator

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["main", "detail"]

class BookDetailForm(ModelForm):
    publication_date_start = forms.DateField(
        widget=DateInput(
            format=('%d/%m/%y'),
            attrs={
                "class": "form-control",
                "placeholder": "Select a date",
                "type": "date"
            }
        ))
    publication_date_end = forms.DateField(
        widget=DateInput(
            format=('%d/%m/%y'),
            attrs={
                "class": "form-control",
                "placeholder": "Select a date",
                "type": "date"
            }
        ))

    price_min = forms.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0.00)])
    price_max = forms.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0.00)])

    class Meta:
        model = BookDetail
        exclude = ("book", "publication_date", "price")

    def __init__(self, *args, **kwargs):
        super(BookDetailForm, self).__init__(*args, **kwargs)
        self.fields["cover"].required = False
        self.fields["publisher"].required = False
        self.fields["description"].required = False
        self.fields["publication_date_start"].required = False
        self.fields["publication_date_end"].required = False
        self.fields["price_min"].required = False
        self.fields["price_max"].required = False

class BookMainForm(ModelForm):
    class Meta:
        model=BookMain
        exclude= ('book',)

    def __init__(self, *args, **kwargs):
        super(BookMainForm, self).__init__(*args, **kwargs)
        self.fields["title"].required = False
        self.fields["author"].required = False