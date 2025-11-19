from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICE_USERS_URL = "http://service-users:5001/users"
SERVICE_ORDERS_URL = "http://service-orders:5002/orders"


@app.route("/users")
def get_users():
    response = requests.get(SERVICE_USERS_URL)
    return jsonify(response.json())


@app.route("/orders")
def get_orders():
    response = requests.get(SERVICE_ORDERS_URL)
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
