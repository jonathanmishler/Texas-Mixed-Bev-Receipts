import json
import urllib3

from config import Settings

settings = Settings()

http = urllib3.PoolManager()

headers = {
    "Accept": "application/json",
    "X-App-Token": settings.tx_app_token
}

params = {
    "$order": "obligation_end_date_yyyymmdd,tabc_permit_number",
    "$limit": 50,
    "$offset": 0
}

url = "https://data.texas.gov/resource/naix-2893.json"

r = http.request(
    "GET",
    url,
    headers = headers,
    fields = params
) 

print(r.geturl())
print(json.loads(r.data.decode('utf-8')))