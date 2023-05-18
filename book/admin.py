from django.contrib import admin
from .models import Book, BookDetail, BookMain

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ["get_main_title", "get_main_author", "get_detail_publication_date"]

    def get_main_title(self, obj):
        return obj.main.title

    def get_main_author(self, obj):
        return obj.main.author

    def get_detail_publication_date(self, obj):
        return obj.detail.publication_date

    get_main_title.admin_order_field = "title"
    get_main_title.short_description = "Title"
    get_main_author.admin_order_field = "author"
    get_main_author.short_description = "Author"
    get_detail_publication_date.admin_order_field = "publication_date"
    get_detail_publication_date.short_description = "Publication Date"

admin.site.register(Book, BookAdmin)
admin.site.register(BookDetail)
admin.site.register(BookMain)

