from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "books"

router = routers.DefaultRouter()
router.register(r"books", views.BookRetrieveViewSet)

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("api/", include((router.urls, "api"))),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
