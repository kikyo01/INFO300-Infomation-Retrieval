from flask import Flask, url_for
from flask import request
from flask import render_template
# import ssl
# import base64
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context

app = Flask(__name__, static_url_path='/static')
# context = create_ssl_context()
# context.check_hostname = False
# context.verify_mode = ssl.CERT_NONE
# home page
# the `/` is the root of your web app
@app.route('/')
def home():
    return render_template('home.html')

# ##   以上显示home page 后端控制

app.route('/search', methods=['get'])
def search():
    keywords = request.args.get('keywords')
#     # Include the keywords in a query object (JSON)
#     query = {
#         "from": 0, "size": 20, 
#         "query": {
#             "multi_match": {
#                 "query": keywords
#             }
#         }
#     }
#  # Send a search request with the query to server
#     res = es.search(index="songch20-author-scrapy-2022-11", body=query)
#     hits = res["hits"]["total"]["value"]
    return render_template('results.html',keywords=keywords)# , keywords=keywords, hits=hits, docs=res["hits"]["hits"]

# es = Elasticsearch(
#     ['219.246.90.69:9200'],
#     http_auth=('elastic', 'oss&&ibm'),
#     scheme="http",
#     port=9200,
#     # ssl_context = context,
# )
if __name__ == "__main__":
    app.run()