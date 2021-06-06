import requests
import json

BASE_URL="http://127.0.0.1:8000/"

data={
    'name':"Genelia",'roll':99,'marks':65
}
json_data=json.dumps(data)
r=requests.post(url=BASE_URL,data=json_data)
data=r.json()
print(r.url)
print(data)

