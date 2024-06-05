from django.urls import path

from catalog.views import (index,
                           FormatsList)

urlpatterns = [
    path("", index, name="index"),
    path(
        "formats/",
        FormatsList.as_view(),
        name="formats_list"
    )
]

app_name = "catalog"

