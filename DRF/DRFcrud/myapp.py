import requests
BASE_URL="http://127.0.0.1:8000/emp/"
r=requests.get(url=BASE_URL)
print(type(r))
print(" r  : ",r,"r.json()  : ",r.json())
print(type(r.json()))



