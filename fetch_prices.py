import requests
from bs4 import BeautifulSoup
import json

# سایت ایرانی bonbast
url = "https://bonbast.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers, timeout=20)
html = r.text

soup = BeautifulSoup(html, "html.parser")

# دلار آزاد
usd = soup.find("td", {"id": "usd1"}).text.strip().replace(",", "")
usd = int(usd)

# اونس جهانی طلا
ounce = soup.find("td", {"id": "goldu"}).text.strip().replace(",", "")
ounce = float(ounce)

result = {
    "usd": usd,
    "ounce": ounce
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("updated:", result)
