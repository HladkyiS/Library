from django.urls import path

from catalog.views import (index,
                           FormatsList,
                           AuthorsList,
                           BooksList,
                           BookDetailView,
                           AuthorDetailView,)

urlpatterns = [
    path("", index, name="index"),
    path(
        "formats/",
        FormatsList.as_view(),
        name="formats_list"
    ),
    path(
        "authors/",
        AuthorsList.as_view(),
        name="authors_list"
    ),
    path(
        "books/",
        BooksList.as_view(),
        name="books_list"
    ),
    path(
        "books/<int:pk>",
        BookDetailView.as_view(),
        name="book_detail"
    ),
    path(
        "authors/<int:pk>",
        AuthorDetailView.as_view(),
        name="author_detail"
    )
]

app_name = "catalog"
