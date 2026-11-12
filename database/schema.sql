
-- =====================================================
-- Projeto: Bondinho da Leitura
-- Banco de dados: bondinho_leitura
-- SGBD: PostgreSQL 18
-- Autor: shunsatsu
-- =====================================================

-- 1. Tabela de livros
CREATE TABLE livro (
    id_livro BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    ano_publicacao SMALLINT,
    descricao TEXT
);

-- 2. Tabela de autores
CREATE TABLE autor (
    id_autor BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(150) NOT NULL
);

-- 3. Associação entre livros e autores
CREATE TABLE livro_autor (
    id_livro BIGINT NOT NULL,
    id_autor BIGINT NOT NULL,

    PRIMARY KEY (id_livro, id_autor),

    FOREIGN KEY (id_livro) REFERENCES livro(id_livro),
    FOREIGN KEY (id_autor) REFERENCES autor(id_autor)
);

-- 4. Tabela de serviços da biblioteca
CREATE TABLE servico (
    id_servico BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    descricao TEXT NOT NULL,
    orientacoes TEXT,
    publicado BOOLEAN NOT NULL DEFAULT TRUE
);

-- 5. Tabela de atividades culturais
CREATE TABLE atividade_cultural (
    id_atividade BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT,
    data_inicio TIMESTAMPTZ NOT NULL,
    data_fim TIMESTAMPTZ NOT NULL,
    local VARCHAR(150),
    publicado BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT chk_data_atividade
        CHECK (data_fim >= data_inicio)
);