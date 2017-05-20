import requests
import json

"""
Section: Get Token
"""

key = "" #<base 64 encoded(yourKey:yourSecret)>

url = "https://plus.dnb.com/v2/token"
data = {"grant_type": "client_credentials"}
headers = {
    "Authorization":
    "Basic " + key,
    "Content-Type": "application/json"
}
res = requests.post(url, headers=headers, json=data).json()
token = res["access_token"]
print token