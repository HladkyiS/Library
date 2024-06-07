from django.shortcuts import render
from django.views import generic

from catalog.models import Book, Author, Format


def index(request):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_formats = Format.objects.count()

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_formats": num_formats
    }

    return render(
        request,
        "catalog/index.html",
        context=context
    )


class FormatsList(generic.ListView):
    model = Format
    template_name = "catalog/formats_list.html"
    context_object_name = "formats"


class AuthorsList(generic.ListView):
    model = Author
    template_name = "catalog/authors_list.html"
    context_object_name = "authors"


class BooksList(generic.ListView):
    model = Book
    template_name = "catalog/books_list.html"
    context_object_name = "books"
    queryset = Book.objects.select_related("format")


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "catalog/book_detail.html"
    context_object_name = "book"
    queryset = Book.objects.select_related("format").prefetch_related("authors")
