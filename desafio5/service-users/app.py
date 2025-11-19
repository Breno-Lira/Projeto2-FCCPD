from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    data = [
        {"id": 1, "name": "Operator"},
        {"id": 2, "name": "Drifter"},
        {"id": 3, "name": "Captain"},
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
