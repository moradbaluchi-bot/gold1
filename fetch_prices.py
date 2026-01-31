import requests
import json

# منبع ایرانی (tgju)
url = "https://api.tgju.org/v1/market/summary"
r = requests.get(url, timeout=20)
data = r.json()

usd = data["data"]["usd"]["price"]
ounce = data["data"]["ounce"]["price"]

result = {
    "usd": usd,
    "ounce": ounce
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("updated:", result)
