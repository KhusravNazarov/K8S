from flask import Flask, jsonify

app = Flask(__name__)

# Sample products
products = [
    {"id": 1, "name": "Loafers", "price": 50},
    {"id": 2, "name": "High Heels", "price": 80},
    {"id": 3, "name": "Boots", "price": 100}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

