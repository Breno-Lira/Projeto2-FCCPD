from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "nome": "Teste1", "joined": "2021-03-15", "active": True},
    {"id": 2, "nome": "Teste2", "joined": "2020-07-02", "active": False},
    {"id": 3, "nome": "Teste3", "joined": "2022-11-20", "active": True}
]

@app.route("/users")
def users():
    return jsonify(USERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
