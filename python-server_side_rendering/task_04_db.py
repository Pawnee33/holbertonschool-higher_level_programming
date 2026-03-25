#!/usr/bin/python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

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
    try:
        with open("items.json", 'r', encoding="utf-8") as f:
            data = json.load(f)
        items = data.get('items', [])
        return render_template('items.html', items=items)
    except FileNotFoundError:
        return "Items file not found", 404
    except json.JSONDecodeError:
        return "Error decoding JSON", 500

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
         with open('products.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
            products = data
    elif source == 'csv':
        with open('products.csv', 'r', newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            products = [
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
                for row in reader
            ]

    elif source == 'sql':
            try:
                connexion = sqlite3.connect('products.db')
                connexion.row_factory = sqlite3.Row
                cursor = connexion.cursor()
                cursor.execute('SELECT id, name, category, price FROM Products')
                rows = cursor.fetchall()
                connexion.close()
                products = [
                    {
                        "id": row["id"],
                        "name": row["name"],
                        "category": row["category"],
                        "price": row["price"]
                    }
                    for row in rows
                ]
            except sqlite3.OperationalError:
                return render_template('product_display.html', error="Database error")

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Product not found")
        filtered = []
        for product in products:
            if int(product["id"]) == product_id:
                filtered.append(product)

        if not filtered:
            return render_template('product_display.html', error="Product not found")
        products = filtered

    return render_template('product_display.html', products=products)
            
if __name__ == '__main__':
    app.run(debug=True, port=5000)
