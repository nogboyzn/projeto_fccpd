from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/health')
def health_check():
    # Custom response structure to avoid generic "hello world"
    return jsonify({
        "status": "operational",
        "service": "node_monitor_v1",
        "message": "Vital signs normal."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
