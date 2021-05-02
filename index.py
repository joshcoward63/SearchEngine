from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from urllib.parse import urlparse
import os
import json
import crawler as cr
import Parser
import requests


url = urlparse('https://paas:c240eae6c4c3a57b62b42aa093239dc4@oin-us-east-1.searchly.com')

es = Elasticsearch(
    [url.hostname],
    http_auth=(url.username, url.password),
    scheme=url.scheme,
    port=443,
)

def create_query(indexName, document):
    global es
    try:
        es.indices.create(index=indexName, ignore=400)
    except :
        print("Index already exsists!")
    res = es.index(index=indexName, body=document)


def search_query(indexName, search_terms):
    global es
    es.indices.refresh(index=indexName)
    # res = es.search(text="test-index", body={"query": {"match_all": {}}})
    res = es.search(index=indexName, body={"query":{"match":{"page":search_terms}}})
    # res = Search().using(es).query("match", title="thus")
    # print("Got %d Hits:" % res['hits']['total']['value'])
    # for hit in res['hits']['hits']:
    #     print("%(page)s: %(page_info)s" % hit["_source"])
    return res['hits']['hits']
    

first_set = cr.get_first("https://www.boisestate.edu/")
urls = cr.get_all_urls(first_set)

for url in urls:
    print(url)
    page = requests.get(url)
    title = Parser.get_title_tags(page)
    body = Parser.get_body_tags(page)
    json_doc = {"header":title,
            "body": body,
            "url": url}
    create_query("live-instance1", json_doc)

# print(search_query("test-index", "python"))