import pytest
from django.urls import reverse
from django.test import Client
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client: Client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro - Home</title>')


def test_email(resp):
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"')


def test_home_link(resp):
    assert_contains(resp, f'<a href="{reverse("base:home")}"')
