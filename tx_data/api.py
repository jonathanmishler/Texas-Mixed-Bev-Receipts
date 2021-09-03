import json
import urllib3

from .config import Settings


class Receipts:
    def __init__(self) -> None:
        self.settings = Settings()
        self.http = urllib3.PoolManager()
        self.url = "https://data.texas.gov/resource/naix-2893.json"
        self.headers = {
            "Accept": "application/json",
            "X-App-Token": self.settings.tx_app_token,
        }
        self.order = "obligation_end_date_yyyymmdd,tabc_permit_number"
        self.limit = 100000
        self.offset = 0

    @property
    def params(self):
        return {
            "$order": self.order,
            "$limit": self.limit,
            "$offset": self.offset,
        }

    def get(self):
        return self.http.request(
            "GET", 
            self.url, 
            headers=self.headers, 
            fields=self.params
        )
