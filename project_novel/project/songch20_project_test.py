from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['219.246.90.69:9200'],
    http_auth=('elastic', 'oss&&ibm'),
    scheme="http",
    port=9200,
    # ssl_context = context,
)
from datetime import datetime
doc = {
    'author': 'Chi Song',
    'text': 'Information Retrieval Systems 2022',
    'timestamp': datetime.now(),
}
print(es.info())
res = es.index("songch20-author-scrapy-2022-11", id=1, body=doc)
print(res['result'])

keywords = "Albert"
query = {
  "from" : 0, "size" : 5,
  "query": {
    "multi_match" : {
      "query": keywords,
      "fields": ["name", "bio" ]
    }
  }
}

res = es.search(index="songch20-author-scrapy-2022-11",body=query)
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(name)s: %(bio)s" % hit["_source"])

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(res["hits"]["hits"])