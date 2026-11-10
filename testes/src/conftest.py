# conftest.py
import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    yield app
    # Código de limpeza pós-teste viria aqui (ex: limpar banco)
 
@pytest.fixture()
def client(app):
    """Um cliente de testes para simular requisições HTTP"""
    return app.test_client()