from database.connection import get_connection


def buscar_livros(termo):
    conexao = get_connection()

    try:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    l.id_livro,
                    l.titulo,
                    l.isbn,
                    l.ano_publicacao,
                    COALESCE(
                        STRING_AGG(DISTINCT a.nome, ', ' ORDER BY a.nome),
                        'Autor não informado'
                    ) AS autores
                FROM livro l
                LEFT JOIN livro_autor la
                    ON l.id_livro = la.id_livro
                LEFT JOIN autor a
                    ON la.id_autor = a.id_autor
                WHERE
                    l.titulo ILIKE %s
                    OR EXISTS (
                        SELECT 1
                        FROM livro_autor la2
                        JOIN autor a2
                            ON la2.id_autor = a2.id_autor
                        WHERE
                            la2.id_livro = l.id_livro
                            AND a2.nome ILIKE %s
                    )
                GROUP BY l.id_livro
                ORDER BY l.titulo;
                """,
                (f"%{termo}%", f"%{termo}%")
            )

            return cursor.fetchall()

    finally:
        conexao.close()