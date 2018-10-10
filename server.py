import json
from flask import Response
from pprint import pprint

from flask import Flask, request
from db.data_layer import create_data, read_data, update_data, delete_data

app = Flask(__name__)

@app.route('/create-data-api', methods=['POST'])
def create_data_api():
    result = create_data(request.form)

    if result != None:
        data = { 'status' : 'success' }
    else:
        data = { 'status' : 'error' }

    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp


@app.route('/read-data-api/<id>', methods=['GET'])
def read_data_api(id):
    result = read_data(id)

    if result != None:
        data = { 'status' : 'success', 'data': result }
    else:
        data = { 'status' : 'error' }

    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp


@app.route('/update-data-api', methods=['POST'])
def update_data_api():
    result = update_data(request.form['id'], request.form)

    if result != None:
        data = { 'status' : 'success' }
    else:
        data = { 'status' : 'error' }

    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp    


@app.route('/delete-data-api', methods=['POST'])
def delete_data_api():
    result = delete_data(request.form['id'])

    if result:
        data = { 'status' : 'success' }
    else:
        data = { 'status' : 'error' }

    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp 


app.run(debug=True)