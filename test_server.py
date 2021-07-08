import requests

BASE = "http://127.0.0.1:5000/"


# test get MSGs history
response = requests.get(BASE + "msg")
print(response.json())

# test post MSG 
response = requests.post(BASE + "msg")
print(response.json())