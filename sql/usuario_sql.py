CRIAR_TABELA_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    habilidades TEXT
);"""


BUSCAR_USUARIO_POR_NOME = """
SELECT * FROM usuario
WHERE nome = ?;
"""

INSERIR_USUARIO = """
INSERT INTO usuario (nome, email, senha, telefone, data_nascimento, habilidades)
VALUES (?, ?, ?, ?, ?, ?);
"""

LISTAR_USUARIOS_POR_HABILIDADES = """
SELECT * FROM usuario
WHERE habilidades LIKE ?;
"""

DELETAR_USUARIO = """
DELETE FROM usuario
WHERE id = ?;
"""

EDITAR_USUARIO = """
UPDATE usuario
SET nome = ?, email = ?, senha = ?, telefone = ?, data_nascimento = ?, habilidades = ?
WHERE id = ?;
"""

LISTAR_USUARIOS_POR_PAGINA = """
SELECT * FROM usuario
LIMIT ? OFFSET ?;
"""
