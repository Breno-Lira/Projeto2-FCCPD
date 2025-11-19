from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
CACHE_HOST = os.getenv("CACHE_HOST")

# Conexão Redis
cache = redis.Redis(host=CACHE_HOST, port=6379, decode_responses=True)

@app.route("/")
def home():
    return "Aplicação rodando! Use /db e /cache"

@app.route("/db")
def db_test():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )

        cur = connection.cursor()
        cur.execute("SELECT NOW();")
        agora = cur.fetchone()[0]

        survivors = read_survivors(connection)
        connection.close()

        survivors_html = "<br>".join([f"{s[0]} - {s[1]}" for s in survivors])

        return f"""
        <h2>Conexão com DB OK!</h2>
        <p>Horário do servidor: {agora}</p>
        <h3>Dados da tabela survivors:</h3>
        <p>{survivors_html}</p>
        """

    except Exception as e:
        return f"Erro no DB: {e}"

def read_survivors(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM survivors;")
    rows = cursor.fetchall()
    cursor.close()
    return rows

@app.route("/cache")
def cache_test():
    try:
        cache.incr("visitas")
        valor = cache.get("visitas")
        return f"Contador Redis: {valor}"
    except Exception as e:
        return f"Erro no Redis: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
