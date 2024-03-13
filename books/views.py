from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book


class HomeView(LoginRequiredMixin, ListView):
    template_name = "books/home.html"
    model = Book
    context_object_name = "books"
