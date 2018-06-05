from flask import Flask, flash, session, request, redirect, render_template, url_for
from db.data_layer import get_all_bills, get_bill, create_bill, delete_bill, update_bill

app = Flask(__name__)

@app.route('/')
def index():
    all_bills = get_all_bills()
    return render_template('index.html', all_bills = all_bills)


@app.route('/add_bill', methods=['POST'])
def add_bill():
    description = request.form['description']
    amount = request.form['amount']
    create_bill(amount, description)
    return redirect(url_for('index'))


@app.route('/delete_bill/<bill_id>')
def delete(bill_id):
    delete_bill(bill_id)
    return redirect(url_for('index'))


@app.route('/edit_bill/<bill_id>', methods=['POST', 'GET'])
def edit_bill(bill_id):
    if request.method == 'POST':
        update_bill(bill_id, request.form['amount'], request.form['description'])
        return redirect(url_for('index'))

    bill = get_bill(bill_id)
    all_bills = get_all_bills()
    return render_template('edit.html', bill = bill, all_bills = all_bills)

app.run(debug=True)