from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

INVENTORY_URL = os.environ.get('INVENTORY_URL', "http://inventory_service:5000/products")

@app.route('/summary')
def get_summary():
    try:
        # Service-to-service communication
        response = requests.get(INVENTORY_URL)
        data = response.json()
        
        # Business Logic: Calculate totals
        total_stock = sum(item['stock'] for item in data)
        item_count = len(data)
        
        return jsonify({
            "report_type": "Inventory Summary",
            "total_items_types": item_count,
            "total_stock_count": total_stock,
            "status": "Computed Successfully"
        })
    except Exception as e:
        return jsonify({"error": f"Failed to fetch inventory: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
