import requests
import time

BASE = "http://127.0.0.1:5000/"

# test get MSGs history
def t_get():
    response = requests.get(BASE + "msg")
    print(response.json())

# test put MSG 
def t_post():
    response = requests.post(BASE + "msg", {"sender": "Jhonny_Xing2000", "payload": "Hello peeps of chatlandia, I'm the new man of the castle"})
    print(response.json())
    response = requests.post(BASE + "msg", {"sender": "FizzBizz", "payload": "Lol, hey jhonny, ye, castle is over there ----------->"})
    print(response.json())
    response = requests.post(BASE + "msg", {"sender": "Jhonny_Xing2000", "payload": "K cya nerd"})
    print(response.json())


t_post()
t_get()