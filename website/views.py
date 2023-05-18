from django.shortcuts import render, redirect
from book.forms import BookForm, BookDetailForm, BookMainForm
from book.models import Book, BookDetail, BookMain
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from website.serializers import UserSerializer, GroupSerializer, BookSerializer

# Create your views here.
def main_view(request):
    context = {}
    template = "main.html"
    if request.method == "GET":
        book_detail_form = BookDetailForm(prefix="detail")
        book_main_form = BookMainForm(prefix="main")
        context["book_detail_form"] = book_detail_form
        context["book_main_form"] = book_main_form
        return render(request, template, context)
    elif request.method == "POST":
        books = Book.objects.select_related("main").select_related("detail").all()
        book_detail_form = BookDetailForm(request.POST, prefix="detail")
        book_main_form = BookMainForm(request.POST, prefix="main")
        if book_detail_form.is_valid() and book_main_form.is_valid():
            title = book_main_form.cleaned_data["title"]
            if title:
                books = books.filter(main__title=title)

            author = book_main_form.cleaned_data["author"]
            if author:
                books = books.filter(main__author=author)

            publisher = book_detail_form.cleaned_data["publisher"]
            if publisher:
                books = books.filter(detail__publisher=publisher)

            cover = book_detail_form.cleaned_data["cover"]
            if cover:
                books = books.filter(detail__cover=cover)

            description = book_detail_form.cleaned_data["description"]
            if description:
                books = books.filter(detail__description=description)

            price_min = book_detail_form.cleaned_data["price_min"]
            price_max = book_detail_form.cleaned_data["price_max"]
            if price_min:
                books = books.filter(detail__price__gte=price_min)
            if price_max:
                books = books.filter(detail__price__lte=price_max)

        publication_date_start = book_detail_form.cleaned_data["publication_date_start"]
        publication_date_end = book_detail_form.cleaned_data["publication_date_end"]
        if publication_date_start:
            books = books.filter(detail__publication_date__gte=publication_date_start)
        if publication_date_end:
            books = books.filter(detail__publication_date__lte=publication_date_end)

        context["books"] = books
        context["book_detail_form"] = book_detail_form
        context["book_main_form"] = book_main_form
        return render(request, template, context)

def book_view(request, pk):
    template="book.html"
    context = {}
    if request.method == "GET":
        book = Book.objects.get(id=pk)
        context["book"] = book
        return render(request, template, context)
    return redirect("main")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        price_min = self.request.query_params.get("price_min")
        if price_min is not None:
            return qs.filter(detail__price__gte=power_min)
        return qs
