import sys
import json
import requests
from bs4 import BeautifulSoup

USERNAME = "doesntmatter1710"

url = f"https://github.com/users/{USERNAME}/contributions"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
if res.status_code != 200:
    print(f"Failed to fetch contributions: {res.status_code}")
    sys.exit(1)

soup = BeautifulSoup(res.text, "html.parser")
days = []

for cell in soup.find_all("td", class_="ContributionCalendar-day"):
    date = cell.get("data-date")
    level = cell.get("data-level", "0")
    if date:
        days.append({"date": date, "level": int(level)})

with open("data/contributions.json", "w") as f:
    json.dump({"days": days}, f, indent=2)

print(f"Fetched {len(days)} contribution days for {USERNAME}!")