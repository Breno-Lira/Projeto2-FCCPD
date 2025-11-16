import sqlite3

connection = sqlite3.connect("/data/banco.db")
cur = connection.cursor()
cur.execute("SELECT * FROM usuarios;")
dados = cur.fetchall()

print("LENDO BANCO EXISTENTE NO VOLUME:")
for linha in dados:
    print(linha)

connection.close()
