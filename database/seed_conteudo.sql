
-- Dados demonstrativos do Bondinho da Leitura

BEGIN;

INSERT INTO servico (nome, descricao, orientacoes)
SELECT dados.nome, dados.descricao, dados.orientacoes
FROM (VALUES
    (
        'Consulta ao catálogo',
        'Consulte informações bibliográficas sobre os livros disponíveis no catálogo demonstrativo.',
        'Utilize a página de consulta de livros.'
    ),
    (
        'Atividades de leitura',
        'Informações demonstrativas sobre atividades de incentivo à leitura.',
        'Consulte a programação cultural para conhecer as atividades cadastradas.'
    ),
    (
        'Orientação ao leitor',
        'Informações para auxiliar os visitantes na descoberta de obras e conteúdos de leitura.',
        'Consulte o catálogo pelo título ou nome do autor.'
    )
) AS dados(nome, descricao, orientacoes)
WHERE NOT EXISTS (
    SELECT 1
    FROM servico s
    WHERE s.nome = dados.nome
);

INSERT INTO atividade_cultural (
    titulo,
    descricao,
    data_inicio,
    data_fim,
    local
)
SELECT
    dados.titulo,
    dados.descricao,
    dados.data_inicio,
    dados.data_fim,
    dados.local
FROM (VALUES
    (
        'Encontro de leitura',
        'Atividade demonstrativa de leitura coletiva e troca de experiências.',
        CURRENT_DATE + INTERVAL '7 days',
        CURRENT_DATE + INTERVAL '7 days 2 hours',
        'Espaço de leitura'
    ),
    (
        'Roda de conversa literária',
        'Atividade demonstrativa para conversar sobre livros e literatura.',
        CURRENT_DATE + INTERVAL '14 days',
        CURRENT_DATE + INTERVAL '14 days 2 hours',
        'Sala de atividades'
    ),
    (
        'Oficina de escrita criativa',
        'Atividade demonstrativa de experimentação e produção textual.',
        CURRENT_DATE + INTERVAL '21 days',
        CURRENT_DATE + INTERVAL '21 days 3 hours',
        'Espaço cultural'
    )
) AS dados(titulo, descricao, data_inicio, data_fim, local)
WHERE NOT EXISTS (
    SELECT 1
    FROM atividade_cultural a
    WHERE a.titulo = dados.titulo
);

COMMIT;
