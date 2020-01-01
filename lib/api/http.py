# Project: Roblox.py
# File: assets.py
# 
# By: Accutrix
# Do not redistribute without proper credit

import requests
import json

class Http:

    def sendRequest(url):
        payload = requests.get(str(url))
        if payload.status_code != 200:
            return print("[Roblox.py][GET] Error: " + payload.status_code)
        return payload.content

    def postRequest(url, payload):
        payload = requests.post(str(url), data = payload)
        if payload.status_code != 200:
            return print("[Roblox.py][POST] Error: " + payload.status_code)
        return payload.content
    
    def format(data):
        return json.loads(data.decode("utf-8"))
