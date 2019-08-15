from datetime import datetime
import requests
import pandas as pd
headers = {'Authorization': 'Bearer aa83e55add1fc19e5e0c16324c0930af'}
url = "https://api.deutschebahn.com/freeplan/v1/departureBoard/8000294?date=2019-08-15T11:00:00"

test = requests.get(url = url, headers = headers).json()

print(pd.DataFrame(test).columns)
print('test')


