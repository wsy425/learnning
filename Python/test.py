import json
import requests
import urllib3
urllib3.disable_warnings()

url = "https://192.168.196.158:5001/api/app/realTimeParam"
# url = "http://www.baidu.com"
r = requests.get(url=url, verify=False)
print("Status Code:", r.status_code)

text = r.text
textjson = json.loads(text)['items']
print("Status Code:", text)
