from django.urls import path

from catalog.views import (index,
                           FormatsList,
                           AuthorsList,)

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
    )
]

app_name = "catalog"

