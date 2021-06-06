import requests
import json
#BASE_URL = "http://127.0.0.1:8000/get/"
def get(id=None):
    data={}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=BASE_URL, data=json_data)  #sending get request to django app#getting respose in r
    django_data = r.json()
    print("Data from django app : ")
    print(django_data)
#get(2)

#BASE_URL = "http://127.0.0.1:8000/post/"

def post_data():
    data={
        'name':"Ritnya",
        'roll':3,
        'marks':65.5
    }
    json_data=json.dumps(data)
    r=requests.post(url=BASE_URL,data=json_data)
    django_response=r.json()
    print(" Response from django application ")
    print(django_response)

#post_data()

BASE_URL = "http://127.0.0.1:8000/update/"
def update_data(id):
    data={'id':id,'name':"Shreya baby",'marks':99.0}
    json_data=json.dumps(data)
    r=requests.put(url=BASE_URL,data=json_data)
    print(r.json())
    print(r.status_code)
    print(r.text)
#update_data(2)

BASE_URL = "http://127.0.0.1:8000/delete/"

def delete_data(id):
    data={'id':id}
    json_data=json.dumps(data)
    r=requests.delete(url=BASE_URL,data=json_data)
    print(r.json())

delete_data(3)







