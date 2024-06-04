from django.contrib import admin

from catalog.models import Book, Author, Format


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "format"]
    list_filter = ["format"]
    search_fields = ["title"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + ("pseudonym",)


admin.site.register(Format)
