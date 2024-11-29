from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

# POST /products: Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        # Validation
        if not name or not description or not isinstance(price, (float, int)):
            return jsonify({'error': 'Invalid input data'}), 400

        # Create product and add to the list
        product = {'id': len(products) + 1, 'name': name, 'description': description, 'price': float(price)}
        products.append(product)
        return jsonify(product), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# GET /products: Retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
