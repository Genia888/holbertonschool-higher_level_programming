from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', "r") as file:
        item = json.load(file)
        items_list = item.get('items', [])
    return render_template('items.html', items=items_list)

def fetch_from_json():
    with open('products.json', "r") as file:
        return json.load(file)

def fetch_from_csv():
    products = []
    with open('products.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['id'] = int(row.get('id', 0))
            row['category'] = row.get('category', 'N/A')
            row['name'] = row.get('name', 'N/A')
            row['price'] = float(row.get('price', 0.0))
            products.append(row)
    return products

def fetch_from_sqlite():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            product = {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": float(row[3])
            }
            products.append(product)
        conn.close()
    except Exception:
        pass
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    products = []
    error = None

    if source == "json":
        try:
            products = fetch_from_json()
        except Exception:
            error = "Error reading JSON file"
    elif source == "csv":
        try:
            products = fetch_from_csv()
        except Exception:
            error = "Error reading CSV file"
    elif source == "sql":
        try:
            products = fetch_from_sqlite()
        except Exception:
            error = "Error reading from database"
    else:
        return render_template('product_display.html', error="Wrong source")

    if not error and product_id:
        products = [product for product in products if int(product.get("id", 0)) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
