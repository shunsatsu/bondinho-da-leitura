
from database.connection import get_connection


def listar_servicos():
    conexao = get_connection()

    try:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    id_servico,
                    nome,
                    descricao,
                    orientacoes
                FROM servico
                WHERE publicado = TRUE
                ORDER BY nome;
            """)

            return cursor.fetchall()

    finally:
        conexao.close()


def listar_atividades():
    conexao = get_connection()

    try:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    id_atividade,
                    titulo,
                    descricao,
                    data_inicio,
                    data_fim,
                    local
                FROM atividade_cultural
                WHERE publicado = TRUE
                  AND data_fim >= CURRENT_TIMESTAMP
                ORDER BY data_inicio;
            """)

            return cursor.fetchall()

    finally:
        conexao.close()
