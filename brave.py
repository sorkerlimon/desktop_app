
from browser_history.browsers import Chrome,Brave
from datetime import datetime

# Fetch history from Chrome
f = Brave()
outputs = f.fetch_history()

# List of (datetime.datetime, url, title, folder) tuples
bms = outputs.histories

# Get today's date
today = datetime.now().date()

# Filter for today's history
today_history = [(timestamp, url, title) for timestamp, url, title in bms if timestamp.date() == today]

# Print the formatted result
for timestamp, url, title in today_history:
    print(f"Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Title: {title}")
    print(f"URL: {url}")
    print("-" * 50)
