#!/usr/bin/python3
"""
Flask application displaying product data from JSON or CSV files.
"""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_data():
    """Reads product data from products.json."""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []


def read_csv_data():
    """Reads product data from products.csv."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception:
        pass
    return products


@app.route('/products')
def display_products():
    """Displays products based on source (json/csv) and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products = read_json_data()
    else:
        products = read_csv_data()

    if product_id:
        try:
            p_id = int(product_id)
            products = [p for p in products if p['id'] == p_id]
            if not products:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                )
        except ValueError:
            return render_template(
                'product_display.html',
                error="Product not found"
            )

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
