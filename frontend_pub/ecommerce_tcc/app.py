import requests 
from flask import Flask, render_template, request, session, redirect, url_for
from .config import get_backend_url


app = Flask(__name__)
app.secret_key = "test123"
BACKEND_URL = get_backend_url()

@app.route('/')
def homepage():
    response = requests.get(BACKEND_URL + "/v1/api/products/")
    catalog = response.json()
    return render_template('homepage.html', catalog=catalog)

@app.route('/cart')
def cart():
    cart = {}
    cart['products'] = []
    cart['total_price'] = 0
    session_cart = session.get('cart', {})
    for product_id in session_cart:
        response = requests.get(BACKEND_URL + f"/v1/api/products/{product_id}")
        product = response.json()
        product_qty = session_cart[product_id]
        cart['products'].append({'product':product,'qty':product_qty})
        cart['total_price'] += int(product['price'])*product_qty
    return render_template('cart.html', cart=cart)

@app.route('/add_to_cart/<pid>', methods=['POST'])
def add_to_cart(pid):
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    if pid not in cart:
        cart[pid] = 1
    else:
        cart[pid] += 1
    session['cart'] = cart 
    return redirect(url_for('homepage'))
        
    
        
