from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book


class HomeView(LoginRequiredMixin, ListView):
    template_name = "books/home.html"
    model = Book
    context_object_name = "books"


class DetailView(LoginRequiredMixin, DetailView):
    template_name = "books/detail.html"
    model = Book
    context_object_name = "book"
