from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def get_inventory():
    # Mock data representing inventory
    return jsonify([
        {"id": 101, "name": "Quantum Processor", "stock": 5},
        {"id": 102, "name": "Dark Matter Fuel", "stock": 12},
        {"id": 103, "name": "Flux Capacitor", "stock": 3}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
