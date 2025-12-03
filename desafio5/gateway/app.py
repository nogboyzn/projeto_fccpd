from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Configuration for downstream services
USER_SERVICE_URL = os.environ.get('USER_SERVICE_URL', 'http://user_service:5000/users')
ORDER_SERVICE_URL = os.environ.get('ORDER_SERVICE_URL', 'http://order_service:5000/orders')

@app.route('/api/users', methods=['GET'])
def gateway_users():
    print(f"Gateway forwarding request to: {USER_SERVICE_URL}", flush=True)
    try:
        resp = requests.get(USER_SERVICE_URL)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": "Gateway Error: User Service Unreachable", "details": str(e)}), 503

@app.route('/api/orders', methods=['GET'])
def gateway_orders():
    print(f"Gateway forwarding request to: {ORDER_SERVICE_URL}", flush=True)
    try:
        resp = requests.get(ORDER_SERVICE_URL)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": "Gateway Error: Order Service Unreachable", "details": str(e)}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
