from datetime import datetime
import requests
import pandas as pd
headers = {'Authorization': 'Bearer aa83e55add1fc19e5e0c16324c0930af'}
url = "https://api.deutschebahn.com/freeplan/v1/departureBoard/8000294?date=2019-09-15T11:00:00"
url2 = "https://api.deutschebahn.com/freeplan/v1/journeyDetails/166983%252F62362%252F878726%252F383702%252F80%253fstation_evaId%253D8000294"

test = pd.DataFrame(requests.get(url = url2, headers = headers).json())

#print(pd.DataFrame(test)['detailsId'][0])
print(test)


