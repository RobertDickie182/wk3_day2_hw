from app import app
from flask import render_template
from models.shop import orders

@app.route('/')
def index():
    return "RC Games"

@app.route('/orders')
def show_all():
    return render_template('index.html', title='Homepage', orders=orders)

@app.route('/orders/order')
def show_order():
    pass