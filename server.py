from flask import Flask, flash, session, request, redirect, render_template
from db.data_layer import get_all_bills, get_bill, create_bill, delete_bill, update_bill

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_bill', methods=['POST'])
def add_bill():
    description = request.form['description']
    amount = request.form['amount']


    create_bill(amount, description)

    all_bills = get_all_bills()
    return render_template('index.html', all_bills = all_bills)

app.run(debug=True)