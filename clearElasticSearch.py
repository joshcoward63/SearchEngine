from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from urllib.parse import urlparse

url = urlparse('https://paas:c240eae6c4c3a57b62b42aa093239dc4@oin-us-east-1.searchly.com')

es = Elasticsearch(
    [url.hostname],
    http_auth=(url.username, url.password),
    scheme=url.scheme,
    port=443,
)


es.indices.delete(index='live-instance1', ignore=[400, 404])



