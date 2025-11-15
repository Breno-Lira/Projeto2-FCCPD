import time
import requests
from datetime import datetime

SERVER_URL = "http://servidor-desafio1:8080/"

while True:
    now = datetime.utcnow().isoformat() + "Z"
    print(f"[{now}] Enviando requisição para {SERVER_URL}")

    try:
        resp = requests.get(SERVER_URL, timeout=5)
        print(f"[{now}] Status: {resp.status_code}")
        print("Resposta:", resp.text)
    except Exception as e:
        print(f"[{now}] Erro ao conectar: {e}")

    print("----")
    time.sleep(5)
