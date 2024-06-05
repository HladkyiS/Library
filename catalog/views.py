from django.shortcuts import render

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
