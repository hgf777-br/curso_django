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
def resp_aula_com_usuario_logado(client_com_usuario_logado, aula):
    return client_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))


def test_titulo(resp_aula_com_usuario_logado, aula: Aula):
    assert_contains(resp_aula_com_usuario_logado, aula.titulo)


def test_vimeo(resp_aula_com_usuario_logado, aula: Aula):
    assert_contains(resp_aula_com_usuario_logado, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"')


def test_modulo_titulo(resp_aula_com_usuario_logado, modulo):
    assert_contains(resp_aula_com_usuario_logado, f'<li class="breadcrumb-item"><a href="{ modulo.get_absolute_url() }">{ modulo.titulo}</a></li>')


@pytest.fixture
def resp_sem_usuario(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_login_redirect(resp_sem_usuario):
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url.startswith(reverse('login'))
