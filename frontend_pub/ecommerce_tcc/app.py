import requests 
from flask import Flask, render_template
from .config import get_backend_url


app = Flask(__name__)
BACKEND_URL = get_backend_url()

@app.route('/')
def homepage():
    response = requests.get(BACKEND_URL + "/v1/api/products/")
    catalog = response.json()
    return render_template('homepage.html', catalog=catalog)

@app.route('/cart')
def cart():
    return render_template('cart.html')
