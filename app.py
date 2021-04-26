from flask import Flask, request, url_for, redirect, render_template
from datetime import datetime
from elasticsearch import Elasticsearch
import os
from urlparse import urlparse
import json
import requests
from elastic_app_search import Client

client = Client(
    base_endpoint='enterprise-search-deployment-d01c1c.ent.us-west1.gcp.cloud.es.io/api/as/v1/',
    api_key='search-9jxtr7r8frnpk89zuy5sdq7w',
    use_https=True
    )
engine_name = 'team5-search-engine'

app = Flask(__name__)

@app.route("/",methods = ['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/<query>")
def result(query):
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['srch']
    res = client.search(engine_name, keyword, {"page": {"size": 100}})
    return render_template('index.html', search_results=res, query=keyword)

if __name__ == "__main__":
	app.run(host="localhost", port=8000, debug=True)