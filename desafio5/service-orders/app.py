from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def orders():
    data = [
        {"id": 101, "user_id": 1, "item": "Drone"},
        {"id": 102, "user_id": 2, "item": "Mochila"},
        {"id": 102, "user_id": 3, "item": "Carga"},

    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
