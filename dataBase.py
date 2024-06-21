# dataBase.py

import sqlite3

def criar_tabela_alunos():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento TEXT,
            data_matricula TEXT,
            filiacao_pai TEXT,
            filiacao_mae TEXT,
            cpf TEXT,
            contato1 TEXT,
            contato2 TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Chama a função para criar a tabela quando este arquivo é executado
if __name__ == "__main__":
    criar_tabela_alunos()

