from flask import Flask, url_for
from flask import request
from flask import render_template
from flask import redirect
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


@app.route('/search', methods=['get'])
def search():
    keywords = request.args.get('keywords')              #args.get('keywords')
    # Include the keywords in a query object (JSON)
    query = {
        "from": 0, "size": 20, 
        "query": {
            "multi_match": {
                "query": keywords
            }
        }
    }
 # Send a search request with the query to server
    res = es.search(index="songch20_project_novel_1-2022-11", body=query)
    hits = res["hits"]["total"]["value"]
    return render_template('results.html', keywords=keywords, hits=hits, docs=res["hits"]["hits"])# , keywords=keywords, hits=hits, docs=res["hits"]["hits"]
es = Elasticsearch(
    ['219.246.90.69:9200'], #'219.246.90.69:9200'           #'210.26.48.81:9201'
    http_auth=('elastic', 'oss&&ibm'),  #elastic #oss&&ibm                           #songch20
    scheme="http",
    port=9200,
    # ssl_context = context,
)
if __name__ == "__main__":
    app.run(debug=True)
