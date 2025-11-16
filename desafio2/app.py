import sqlite3
import os

DB_PATH = "/data/banco.db"

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

conection = sqlite3.connect(DB_PATH)
cursor = conection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    );
""")

cursor.execute("INSERT INTO usuarios (nome) VALUES ('Teste1');")
cursor.execute("INSERT INTO usuarios (nome) VALUES ('Teste2');")

cursor.execute("SELECT * FROM usuarios;")
dados = cursor.fetchall()


print("Conteúdo persistido no banco:")
for linha in dados:
    print(linha)

conection.commit()
conection.close()
