from django.db import models


class Format(models.Model):
    # Book format

    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    pseudonym = models.CharField(max_length=63, null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    format = models.ForeignKey(
        Format,
        on_delete=models.CASCADE,
        related_name="books"
    )

    authors = models.ManyToManyField(
        Author,
        related_name="books"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} (format: {self.format.name})"

