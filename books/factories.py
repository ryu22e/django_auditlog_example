import factory

from .models import Book


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence", nb_words=4)
    price = factory.Faker("random_int", min=10, max=5000)
