from flask import Flask, request, url_for, redirect, render_template
from datetime import datetime
from elasticsearch import Elasticsearch
import os
from urlparse import urlparse
import json
import requests

es = Elasticsearch(['https://paas:c240eae6c4c3a57b62b42aa093239dc4@oin-us-east-1.searchly.com'])

res = es.get(index="test-index2", id=1)
print(res['_source'])

es.indices.refresh(index="test-index2")

app = Flask(__name__)

@app.route("/",methods = ['POST', 'GET'])
def home():
    return render_template("index.html")

@app.route("/<query>")
def result(query):
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
	return render_template("aboutus.html")

@app.route('/search',methods = ['POST', 'GET'])
def search():
	if request.method == 'POST':
		string = request.form['srch']
		doc = {'size' : 10000, "query" : {"match": {"name" : string}}}
		res = es.search(index='test-index2', body=doc,scroll='1m')
		result = "%d" % res['hits']['total']['value']
		resultText = ''
		for hit in res['hits']['hits']:
			resultText += str(hit['_source']['name']) + ': \n'
		if (result == '0'):
			return render_template('results.html', processed_text="No results found")
		else:
			return render_template('results.html', processed_text=result+" result(s) found\n" +resultText)
		
	else:
		string = request.args.get('srch')
		return redirect(url_for('result',query = string))

if __name__ == "__main__":
	app.run(host="localhost", port=8000, debug=True)