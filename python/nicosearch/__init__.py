#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import requests
import json
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin  = codecs.getreader('utf_8')(sys.stdin)

url = 'http://api.search.nicovideo.jp/api/'
payload = {
  "query":u"閃乱カグラ",
  "service":[ "video" ],
  "search":[ "title" ],
  "join":[ "cmsid",
  "title",
  "view_counter" ],
  "from":0,
  "size":10,
  "sort_by":"view_counter",
  "issuer":"apiguide",
  "reason":"ma9"
}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
print r.text

class SearchQueryBuilder():
    def __init__(self, query, service, search, join, title, view_counter, from, size, sort_by, issuer, reason):
        pass
    def build(self):
        return SearchRequest()

class SearchRequest():
    def __init__(self, data, url):
        self.data = 
        pass
    def fetch(self):
        return SearchResponse()

class SearchResponse():
    def __init__(self):
        pass
    def get(self):
        pass

SeqrchRequest(SearchRequestBuilder().build(), url).fetch().get('contents').filter()

from flask import Flask
app = Flask(__name__)
from flask import render_template

@app.route("/")
def hello():
    return render_template('index.html', hoge=r.text)

if __name__ == "__main__":
    app.run()
