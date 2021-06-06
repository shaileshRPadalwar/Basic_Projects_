import requests
import json

URL="http://127.0.0.1:8000/get/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        resp=requests.get(url=URL,data=json_data)
        print(resp.json())
    json_data=json.dumps(data)
    resp=requests.get(url=URL,data=json_data)
    print(resp.json())

#get_data()

def post_data():
    URL = "http://127.0.0.1:8000/post/"
    data={'name':"Ananya Pande",'roll':3,'marks':74}
    json_data=json.dumps(data)
    resp=requests.post(url=URL,data=json_data)
    print(resp.json())
#post_data()

def delete_data(id):
    URL = "http://127.0.0.1:8000/delete/"
    data={'id':id}
    json_data=json.dumps(data)
    resp=requests.post(url=URL,data=json_data)
    print(resp.json())
#delete_data(1)


def update_data(id=None):
    URL= "http://127.0.0.1:8000/update/"
    data={'id':id,'name':"Allu Arjun"}
    json_data=json.dumps(data)
    resp=requests.put(url=URL,data=json_data)
    print(resp.json())

update_data(2)















