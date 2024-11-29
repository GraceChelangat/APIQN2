import requests

BASE_URL = 'http://127.0.0.1:5000'

def add_product(name, description, price):
    url = f"{BASE_URL}/products"
    data = {'name': name, 'description': description, 'price': price}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Product created successfully:", response.json())
    else:
        print("Failed to create product:", response.json())

def list_products():
    url = f"{BASE_URL}/products"
    response = requests.get(url)
    if response.status_code == 200:
        print("Products List:", response.json())
    else:
        print("Failed to retrieve products:", response.json())

if __name__ == '__main__':
    # Add products
    add_product("Tea", "A refreshing tea product", 3.5)
    add_product("Coffee", "Premium coffee beans", 5.0)

    # List all products
    list_products()
