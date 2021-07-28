import json
import requests

from vandelay_app.config import API_KEY, API_SECRET
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth(API_KEY, API_SECRET)

headers = {
'Authorization': 'Basic ' + API_KEY,
'Content-Type': 'application/json'
}

def get_url(url):
    return requests.get(url, auth=auth)


def post_url(url, values):
    if not values:
        values = dict()
    return requests.post(url, auth=auth, json=values)


def delete_url(url, values):
    if not values:
        values = dict()
    return requests.delete(url, auth=auth, json=values)


def dump(response):
    print(json.dumps(response.json()))


