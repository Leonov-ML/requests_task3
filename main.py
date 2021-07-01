import os

import requests

from datetime import datetime, timedelta

today = datetime.now()
two_days_before = today - timedelta(2)

API_URL = "https://api.stackexchange.com/2.3/questions"
TAG = "Python"

response = requests.get(API_URL, params={"fromdate": int(two_days_before.timestamp()),
                                         "tagged": TAG,
                                         "site": "stackoverflow"})
response.raise_for_status()
items = response.json()["items"]
service = open(f"topics for_{today}.txt", "w+", encoding='utf-8')
for item in items:
    print(item["title"])
    service.write(f'{item["title"]}\n')
