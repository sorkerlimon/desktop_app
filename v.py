import browserhistory as bh
from datetime import datetime

dict_obj = bh.get_browserhistory()
today = datetime.now().date()
chrome_data = [i for i in dict_obj['chrome'] if i[2].date() == today]
print(chrome_data)

WGNlpenozCZw4&Dqcj