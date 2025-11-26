from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

SERVICE_A_URL = os.getenv("SERVICE_A_URL", "http://service-a:5000")

@app.route("/completo")
def completo():
    try:
        r = requests.get(f"{SERVICE_A_URL}/users", timeout=5)
        r.raise_for_status()
    except Exception as e:
        return jsonify({"error": "failed to fetch from service A", "details": str(e)}), 502

    users = r.json()
    
    out = []
    for u in users:
        status = "ativo" if u.get("active") else "inativo"
        out.append({
            "id": u.get("id"),
            "mensagem": f"Usuario {u.get('nome')} ({status}) - ingresou em {u.get('joined')}"
        })
    return jsonify(out)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
