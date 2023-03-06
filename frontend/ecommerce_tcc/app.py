import requests 
from flask import Flask, render_template, request, url_for, redirect
from .config import get_backend_url


app = Flask(__name__)
BACKEND_URL = get_backend_url()

@app.route('/')
def homepage():
    response = requests.get(BACKEND_URL + "/v1/api/products/")
    catalog = response.json()
    return render_template('homepage.html', catalog=catalog)

@app.route('/warehouse')
def warehouse():
    response = requests.get(BACKEND_URL + "/v1/api/products/")
    catalog = response.json()
    return render_template('warehouse.html', catalog=catalog)

@app.route('/cart')
def cart():
    return render_template('cart.html')

# TO DO: VALIDAR O ERRO
@app.route('/product', methods=('GET', 'POST'))
def product():
    if request.method == 'GET':
        return render_template('new_product.html')
    elif request.method == 'POST':
        new_product = {}
        new_product["sku"] = request.form['sku']
        new_product["desc"] = request.form['description']
        new_product["photo"] = request.form['photo']
        new_product["available_qty"] = int(request.form['quantity'])
        new_product["price"] = request.form['price']
        response = requests.post(BACKEND_URL + "/v1/api/products/", json=new_product)
        return redirect(url_for('warehouse'))

@app.route('/product/<int:pid>', methods=('DELETE',))
def delete_product(pid):
    response = requests.delete(BACKEND_URL + f"/v1/api/products/{pid}")
    return redirect(url_for('warehouse'))
    
    
