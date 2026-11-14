
-- Projeto: Bondinho da Leitura
-- Dados demonstrativos para desenvolvimento e testes

BEGIN;

-- Autores
INSERT INTO autor (nome)
SELECT dados.nome
FROM (VALUES
    ('Neil Gaiman'),
    ('Machado de Assis'),
    ('Jane Austen'),
    ('Mary Shelley'),
    ('Arthur Conan Doyle')
) AS dados(nome)
WHERE NOT EXISTS (
    SELECT 1 FROM autor a WHERE a.nome = dados.nome
);

-- Livros
INSERT INTO livro (titulo, ano_publicacao)
SELECT dados.titulo, dados.ano_publicacao
FROM (VALUES
    ('Absolute Sandman', 2006),
    ('Dom Casmurro', 1899),
    ('O Alienista', 1882),
    ('Orgulho e Preconceito', 1813),
    ('Frankenstein', 1818),
    ('As Aventuras de Sherlock Holmes', 1892)
) AS dados(titulo, ano_publicacao)
WHERE NOT EXISTS (
    SELECT 1 FROM livro l WHERE l.titulo = dados.titulo
);

-- Associação entre livros e autores
INSERT INTO livro_autor (id_livro, id_autor)
SELECT l.id_livro, a.id_autor
FROM (VALUES
    ('Absolute Sandman', 'Neil Gaiman'),
    ('Dom Casmurro', 'Machado de Assis'),
    ('O Alienista', 'Machado de Assis'),
    ('Orgulho e Preconceito', 'Jane Austen'),
    ('Frankenstein', 'Mary Shelley'),
    ('As Aventuras de Sherlock Holmes', 'Arthur Conan Doyle')
) AS dados(titulo, autor)
JOIN livro l ON l.titulo = dados.titulo
JOIN autor a ON a.nome = dados.autor
ON CONFLICT (id_livro, id_autor) DO NOTHING;

COMMIT;
