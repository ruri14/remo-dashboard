from django.db import models
import urllib.request
import json
from app2.remo_token import token

def get_state():
    url = "https://api.nature.global/1/devices"
    req_header = {
        'accept': 'application/json',
        'Authorization': 'Bearer '+token.token
    }
    req = urllib.request.Request(url, method='GET', headers=req_header)
    with urllib.request.urlopen(req) as response:
        body = json.loads(response.read())
        il = body[0]['newest_events']['il']['val']
        te = body[0]['newest_events']['te']['val']
        hu = body[0]['newest_events']['hu']['val']
        mo = body[0]['newest_events']['mo']['val']
    return [il, te, hu, mo]
 

def signal_send(signal_id):
    url = "https://api.nature.global/1/signals/"+signal_id+"/send"
    req_header = {
        'accept': 'application/json',
        'Authorization': 'Bearer '+token.token
    }
    req = urllib.request.Request(url, method='POST', headers=req_header)
    with urllib.request.urlopen(req) as response:
        body = json.loads(response.read())


def aircon_settings(appliance_id, data):
    url = "https://api.nature.global/1/appliances/"+appliance_id+"/aircon_settings"
    req_header = {
        'accept': 'application/json',
        'Authorization': 'Bearer '+token.token
    }
    data_encode = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=data_encode, method='POST', headers=req_header)
    with urllib.request.urlopen(req) as response:
        body = json.loads(response.read())
