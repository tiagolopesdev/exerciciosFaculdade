import sqlite3 as sql

conn = sql.connect('aulaDB.db')
print(type(conn))

ddlCreate = """CREATE TABLE fornecedor (
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    conn = sqlite3.connect('aulaDB.db')
    nome_fornecedor TEXT NOT NULL,
    print(type(conn))
    cnpj VARCHAR(18) NOT NULL,
    cidade TEXT,
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL
);"""

cursor = conn.cursor()
cursor.execute(ddlCreate)
print(type(cursor))

print("Tabela criada!")
print("Descricao do cursor: "+cursor.description)
print("Linhas afetadas:"+cursor.rowcount)
cursor.close()
conn.close()
