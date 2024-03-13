from django.urls import reverse
from pytest_django.asserts import assertRedirects


def test_show_home_page(client, django_user_model):
    username = "user"
    password = "testpass"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.force_login(user)

    actual = client.get(reverse("books:home"))

    assert actual.status_code == 200


def test_redirect_to_login_page_when_accessing_home_page_without_login(client, db):
    actual = client.get(reverse("books:home"))

    assertRedirects(actual, reverse("login") + "?next=" + reverse("books:home"))


def test_show_detail_page(client, django_user_model, book_factory):
    username = "user"
    password = "testpass"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.force_login(user)
    book = book_factory()

    actual = client.get(reverse("books:detail", kwargs={"pk": book.pk}))

    assert actual.status_code == 200


def test_redirect_to_login_page_when_accessing_detail_page_without_login(
    client, db, book_factory
):
    book = book_factory()
    url = reverse("books:detail", kwargs={"pk": book.pk})

    actual = client.get(url)

    assertRedirects(actual, reverse("login") + "?next=" + url)
