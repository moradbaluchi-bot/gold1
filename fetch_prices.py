import requests
from bs4 import BeautifulSoup
import json
import re

headers = {"User-Agent": "Mozilla/5.0"}

def get_from_bonbast():
    url = "https://bonbast.com"
    r = requests.get(url, headers=headers, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")

    usd_tag = soup.find("td", {"id": "usd1"})
    gold_tag = soup.find("td", {"id": "goldu"})

    if not usd_tag or not gold_tag:
        return None

    usd_text = usd_tag.text
    gold_text = gold_tag.text

    usd = int(re.sub(r"[^\d]", "", usd_text))
    ounce = float(re.sub(r"[^\d.]", "", gold_text))

    return usd, ounce


def get_from_tgju_html():
    url = "https://www.tgju.org"
    r = requests.get(url, headers=headers, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")

    usd_tag = soup.select_one(".market-price span")
    ounce_tag = soup.select_one("span#ounce")

    if not usd_tag or not ounce_tag:
        return None

    usd = int(re.sub(r"[^\d]", "", usd_tag.text))
    ounce = float(re.sub(r"[^\d.]", "", ounce_tag.text))

    return usd, ounce


data = None

try:
    data = get_from_bonbast()
except:
    data = None

if not data:
    try:
        data = get_from_tgju_html()
    except:
        data = None

if not data:
    raise Exception("No source returned valid data")

usd, ounce = data

result = {"usd": usd, "ounce": ounce}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("UPDATED:", result)
