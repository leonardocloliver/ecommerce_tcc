import requests 
from flask import Flask, render_template, request, url_for, redirect, make_response
from .config import get_backend_url


app = Flask(__name__)
BACKEND_URL = get_backend_url()

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and  password == 'password':
            resp = make_response(redirect(url_for('warehouse')))
            resp.set_cookie('username', username)
            return resp
        else:
            error = "Credenciais invalidas. Tente novamente"
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('username')
    return resp

@app.route('/')
def warehouse():
    username = request.cookies.get('username')
    if username:
        response = requests.get(BACKEND_URL + "/v1/api/products/")
        catalog = response.json()
        return render_template('warehouse.html', catalog=catalog)
    else:
        return redirect(url_for('login'))

@app.route('/product', methods=['GET', 'POST'])
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

@app.route('/delete_product/<pid>', methods=['GET'])
def delete_product(pid):
    response = requests.delete(BACKEND_URL + f"/v1/api/products/{pid}")
    return redirect(url_for('warehouse'))

@app.route('/update_product/<pid>', methods=['GET', 'POST'])
def update_product(pid):
    if request.method == 'GET':
        response = requests.get(BACKEND_URL + f"/v1/api/products/{pid}")
        product = response.json()
        return render_template('update_product.html', product=product)
    elif request.method == 'POST':
        update_product = {}
        update_product["sku"] = request.form['sku']
        update_product["desc"] = request.form['description']
        update_product["photo"] = request.form['photo']
        update_product["available_qty"] = int(request.form['quantity'])
        update_product["price"] = request.form['price']
        response = requests.put(BACKEND_URL + f"/v1/api/products/{pid}", json=update_product)
        return redirect(url_for('warehouse'))
