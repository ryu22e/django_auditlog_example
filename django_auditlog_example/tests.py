import pytest
from pytest_django.asserts import assertRedirects
from django.urls import reverse


def test_show_home_page(client):
    actual = client.get(reverse("home"))

    assert actual.status_code == 200


def test_show_login_page(client):
    actual = client.get(reverse("login"))

    actual.status_code == 200


@pytest.mark.django_db
def test_redirect_to_home_page_if_login(client, django_user_model):
    username = "test"
    password = "testpass"
    django_user_model.objects.create_user(username=username, password=password)
    params = {"username": username, "password": password}

    actual = client.post(reverse("login"), params)

    assertRedirects(actual, reverse("home"))


def test_redirect_to_login_page_if_logout(client):
    actual = client.post(reverse("logout"))

    assertRedirects(actual, reverse("login"))
