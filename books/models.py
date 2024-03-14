from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})
