import requests, json

url = "http://127.0.0.1:8000/upload_passengers"
with open("sample.json") as f:
    payload = json.load(f)

res = requests.post(url, json=payload)
print(res.json())
