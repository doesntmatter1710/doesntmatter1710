import os
import json
import requests

USERNAME = "doesntmatter1710"
# Set GITHUB_TOKEN in your environment or paste a classic token here
TOKEN = os.getenv("GH_PAT", "")

if not TOKEN:
    print("Warning: GH_PAT not found. Falling back to public API fetch.")

query = """
query($username: String!) {
  user(login: $username) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
            color
          }
        }
      }
    }
  }
}
"""

def fetch_via_api():
    headers = {"Authorization": f"bearer {TOKEN}"} if TOKEN else {}
    url = "https://api.github.com/graphql"
    response = requests.post(
        url, 
        json={"query": query, "variables": {"username": USERNAME}}, 
        headers=headers
    )
    
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return None

    res_data = response.json()
    weeks = res_data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    
    days_data = []
    for week in weeks:
        for day in week["contributionDays"]:
            count = day["contributionCount"]
            # Map contribution count to 0-4 intensity level
            level = 0
            if count > 0: level = 1
            if count > 3: level = 2
            if count > 6: level = 3
            if count > 10: level = 4

            days_data.append({
                "date": day["date"],
                "count": count,
                "level": level
            })

    return {"days": days_data}

data = fetch_via_api()

if data:
    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Successfully fetched accurate contribution data!")