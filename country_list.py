import json
import urllib.request

url = "https://free.currconv.com/api/v7/currencies?apiKey=d5d687fa6c9b6ac1836f"
json_obj = urllib.request.urlopen(url)
data = json.load(json_obj)

inside_data = data['results']
cur_list = []
for item in inside_data.values():
    cur_str = item['id'] + ", " + item['currencyName']
    cur_list.append(cur_str)

print(cur_list)