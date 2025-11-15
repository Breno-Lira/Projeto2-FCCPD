from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "msg": "Mensagem de sucesso: ta pegando",
        "time": datetime.utcnow().isoformat() + "Z",
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
