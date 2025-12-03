from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders')
def get_orders():
    return jsonify([
        {"order_id": "ORD-991", "item": "Neural Interface", "cost": 4500.00},
        {"order_id": "ORD-992", "item": "Holographic Projector", "cost": 299.99}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
