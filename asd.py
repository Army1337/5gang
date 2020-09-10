import requests

import json

url = "https://www.otlob.com/apiweb/v1/account/login"
datas = {"username": "test@Test.com", "password": "aaaaaaaaaaaaa", "rememberMe": "false"}
headers = {"content-type": "application/json;charset=UTF-8",
"accept": "application/json, text/plain, */*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US",
"origin": "https://www.otlob.com",
"referer": "https://www.otlob.com/",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
api_sender = requests.session()
rsp = api_sender.post(url, json=datas, headers=headers)

if ""result":"Unknown exception, please contact the customer service.","code":-99" in rsp.content:
	print("failed")