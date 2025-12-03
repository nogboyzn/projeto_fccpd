from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def get_users():
    return jsonify([
        {"id": 1, "username": "cyber_alice", "role": "sysadmin"},
        {"id": 2, "username": "crypto_bob", "role": "analyst"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
