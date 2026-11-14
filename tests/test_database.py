
from database.connection import get_connection
from services.livro_service import buscar_livros
from services.conteudo_service import listar_servicos, listar_atividades


def test_conexao_postgresql():
    conexao = get_connection()

    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT current_database() AS nome")
            resultado = cursor.fetchone()

        assert resultado["nome"] == "bondinho_leitura"

    finally:
        conexao.close()


def test_busca_livros_no_banco():
    livros = buscar_livros("Machado")

    assert len(livros) >= 2
    assert any(
        livro["titulo"] == "Dom Casmurro"
        for livro in livros
    )


def test_consulta_servicos_no_banco():
    servicos = listar_servicos()

    assert len(servicos) >= 1
    assert any(
        servico["nome"] == "Consulta ao catálogo"
        for servico in servicos
    )


def test_consulta_atividades_no_banco():
    atividades = listar_atividades()

    assert len(atividades) >= 1
    assert any(
        atividade["titulo"] == "Encontro de leitura"
        for atividade in atividades
    )

def test_busca_livros_nao_executa_sql_injetado():
    termo = "' OR '1'='1"

    livros = buscar_livros(termo)

    assert livros == []
