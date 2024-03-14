from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from auditlog.mixins import LogAccessMixin
from auditlog.signals import accessed

from .models import Book
from .serializers import BookSerializer


class HomeView(LoginRequiredMixin, ListView):
    template_name = "books/home.html"
    model = Book
    context_object_name = "books"


class DetailView(LogAccessMixin, LoginRequiredMixin, DetailView):
    template_name = "books/detail.html"
    model = Book
    context_object_name = "book"


class BookRetrieveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = super().get_object()
        accessed.send(sender=obj.__class__, instance=obj)
        return obj
