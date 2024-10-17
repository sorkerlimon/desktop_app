# import sqlite3
# import os
# import datetime
# from pathlib import Path
# import shutil
# import tempfile

# def get_chrome_history_today():
#     # Path to Chrome's history database
#     history_db = Path(os.getenv('LOCALAPPDATA')) / r"Google\Chrome\User Data\Default\History"
    
#     # Ensure the database exists
#     if not history_db.is_file():
#         print("Chrome history database not found.")
#         return []
    
#     # Create a temporary copy of the database
#     temp_dir = tempfile.mkdtemp()
#     temp_history_db = Path(temp_dir) / "TempHistory"
#     shutil.copy2(history_db, temp_history_db)
    
#     try:
#         # Connect to the temporary database
#         conn = sqlite3.connect(temp_history_db)
#         cursor = conn.cursor()
        
#         # Get today's date
#         today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
#         # Convert today's date to microseconds since epoch
#         today_microseconds = int(today.timestamp() * 1000000)
        
#         # Query to get today's history
#         query = """
#         SELECT url, title, datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime') as visit_time
#         FROM urls
#         WHERE last_visit_time > ?
#         ORDER BY last_visit_time DESC
#         """
        
#         cursor.execute(query, (today_microseconds,))
        
#         # Fetch all results
#         results = cursor.fetchall()
        
#         # Close the connection
#         conn.close()
        
#         return results
    
#     finally:
#         # Clean up: remove the temporary directory and its contents
#         shutil.rmtree(temp_dir)

# if __name__ == "__main__":
#     print("Chrome browser history for today:")
#     for url, title, visit_time in get_chrome_history_today():
#         print(f"Time: {visit_time}")
#         print(f"Title: {title}")
#         print(f"URL: {url}")
#         print("-" * 50)
        



from browser_history.browsers import Chrome
from datetime import datetime

# Fetch history from Chrome
f = Chrome()
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
