from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return self.title
