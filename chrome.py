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
        

        # print(f"Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        # print(f"Title: {title}")
        # print(f"URL: {url}")
        # print("-" * 50)


# from browser_history.browsers import Chrome
# from datetime import datetime


# f = Chrome()
# outputs = f.fetch_history()
# bms = outputs.histories
# today = datetime.now().date()
# today_history = [(timestamp, url, title) for timestamp, url, title in bms if timestamp.date() == today]
# with open("chrome_history.txt", "w",encoding="utf-8") as f:
#     for timestamp, url, title in today_history:


#         f.write(f"Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n")
#         f.write(f"Title: {title}\n")
#         f.write(f"URL: {url}\n")
#         f.write("-" * 50 + "\n")



from browser_history.browsers import Chrome
from datetime import datetime, time

# Fetch the browsing history
f = Chrome()
outputs = f.fetch_history()
bms = outputs.histories

start_time = time(11, 0)  # 3:00 PM
end_time = time(16, 0)    # 4:00 PM

# Filter history for today within the time range from 3:00 PM to 4:00 PM
specific_time_history = [
    (timestamp, url, title)
    for timestamp, url, title in bms
    if timestamp.date() == datetime.now().date() and start_time <= timestamp.time() < end_time
]

# Write the filtered history to a file
with open("chrome_specific_time_history.txt", "w", encoding="utf-8") as f:
    for timestamp, url, title in specific_time_history:
        f.write(f"Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Title: {title}\n")
        f.write(f"URL: {url}\n")
        f.write("-" * 50 + "\n")



# from browser_history.browsers import Chrome, Brave
# from datetime import datetime, time
# import asyncio

# # Async function to fetch and filter Chrome history continuously
# async def fetch_chrome_history():
#     while True:
#         f = Chrome()
#         outputs = f.fetch_history()
#         bms = outputs.histories

#         # Set the specific time range (e.g., from 3:00 PM to 4:00 PM)
#         start_time = time(15, 0)  # 3:00 PM
#         end_time = time(16, 0)    # 4:00 PM

#         # Filter history for today within the time range
#         specific_time_history = [
#             (timestamp, url, title)
#             for timestamp, url, title in bms
#             if timestamp.date() == datetime.now().date() and start_time <= timestamp.time() < end_time
#         ]

#         # Write the filtered history to a file
#         with open("chrome_specific_time_history.txt", "w", encoding="utf-8") as f:
#             for timestamp, url, title in specific_time_history:
#                 f.write(f"Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n")
#                 f.write(f"Title: {title}\n")
#                 f.write(f"URL: {url}\n")
#                 f.write("-" * 50 + "\n")

#         # Short pause before checking again (optional, can set lower for near-real-time)
#         await asyncio.sleep(1)  # Check again after 1 second (can be lower for near-instant checking)

# # Async function to fetch and filter Brave history continuously
# async def fetch_brave_history():
#     while True:
#         f = Brave()
#         outputs = f.fetch_history()
#         bms = outputs.histories

#         # Set the specific time range (e.g., from 3:00 PM to 4:00 PM)
#         start_time = time(15, 0)  # 3:00 PM
#         end_time = time(16, 0)    # 4:00 PM

#         # Filter history for today within the time range
#         specific_time_history = [
#             (timestamp, url, title)
#             for timestamp, url, title in bms
#             if timestamp.date() == datetime.now().date() and start_time <= timestamp.time() < end_time
#         ]

#         # Write the filtered history to a file
#         with open("brave_specific_time_history.txt", "w", encoding="utf-8") as f:
#             for timestamp, url, title in specific_time_history:
#                 f.write(f"Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n")
#                 f.write(f"Title: {title}\n")
#                 f.write(f"URL: {url}\n")
#                 f.write("-" * 50 + "\n")

#         # Short pause before checking again (optional)
#         await asyncio.sleep(1)  # Check again after 1 second

# # Main function to run both async tasks concurrently
# async def main():
#     # Schedule both async functions to run concurrently
#     await asyncio.gather(
#         fetch_chrome_history(),
#         fetch_brave_history()
#     )

# # Run the main async function
# asyncio.run(main())
