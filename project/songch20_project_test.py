from elasticsearch import Elasticsearch
es = Elasticsearch(
  #王神服务器 219.246.90.69:9200
  #信息院服务器  210.26.48.81:9201
    ['210.26.48.81:9201'],
    http_auth=('songch20', 'songch20'),
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

keywords = "我们"
query = {
  "from" : 0, "size" : 5,
  "query": {
    "multi_match" : {
      "query": keywords
    }
  }
}

res = es.search(index="songch20_project_novel-2022-11",body=query)
print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(name)s: %(bio)s" % hit["_source"])

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(res["hits"]["hits"])
docs = res["hits"]["hits"]
for doc in docs:
  print(doc["_source"]['Title'])
  print(doc["_source"]['Author'])
  print(doc["_source"]['Score'])
  print(doc["_source"]['Publishing_house'])
  print(doc["_source"]['Year_of_publication'])
  print(doc["_source"]['Number_of_pages'])
  print(doc["_source"]['ISBN'])
  print(type(doc["_source"]['Brief_introduction']))
  print("-----------------------")
