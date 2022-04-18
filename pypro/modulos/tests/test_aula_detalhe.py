import pytest
from django.urls import reverse
from model_bakery import baker
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula, Modulo


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo, db):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"')


def test_modulo_titulo(resp, modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{ modulo.get_absolute_url() }">{ modulo.titulo}</a></li>')
