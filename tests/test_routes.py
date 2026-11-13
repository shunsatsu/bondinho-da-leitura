
import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_pagina_inicial(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert b"Bondinho da Leitura" in resposta.data
    assert b"Consultar livros" in resposta.data


def test_pagina_de_livros(client, monkeypatch):
    from controllers import livros_controller

    def buscar_livros_fake(termo):
        return [
            {
                "id_livro": 1,
                "titulo": "Dom Casmurro",
                "isbn": None,
                "ano_publicacao": 1899,
                "autores": "Machado de Assis"
            }
        ]

    monkeypatch.setattr(
        livros_controller,
        "buscar_livros",
        buscar_livros_fake
    )

    resposta = client.get("/livros?q=Machado")

    assert resposta.status_code == 200
    assert b"Dom Casmurro" in resposta.data
    assert b"Machado de Assis" in resposta.data


def test_pagina_de_servicos(client, monkeypatch):
    from controllers import conteudo_controller

    def listar_servicos_fake():
        return [
            {
                "id_servico": 1,
                "nome": "Consulta ao catálogo",
                "descricao": "Consulte os livros.",
                "orientacoes": "Utilize a pesquisa."
            }
        ]

    monkeypatch.setattr(
        conteudo_controller,
        "listar_servicos",
        listar_servicos_fake
    )

    resposta = client.get("/servicos")

    assert resposta.status_code == 200
    assert b"Consulta ao cat" in resposta.data


def test_pagina_de_programacao(client, monkeypatch):
    from controllers import conteudo_controller
    from datetime import datetime, timezone

    def listar_atividades_fake():
        return [
            {
                "id_atividade": 1,
                "titulo": "Encontro de leitura",
                "descricao": "Leitura coletiva.",
                "data_inicio": datetime(2027, 1, 10, 14, 0, tzinfo=timezone.utc),
                "data_fim": datetime(2027, 1, 10, 16, 0, tzinfo=timezone.utc),
                "local": "Espaço de leitura"
            }
        ]

    monkeypatch.setattr(
        conteudo_controller,
        "listar_atividades",
        listar_atividades_fake
    )

    resposta = client.get("/programacao")

    assert resposta.status_code == 200
    assert b"Encontro de leitura" in resposta.data
    assert b"Espa" in resposta.data
