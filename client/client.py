import requests

import time

BASE = "http://127.0.0.1:5000/"

def single_cycle():
    response = requests.get(BASE + "msg")
    print(response.json())
    time.sleep(1)










##################################
#             MAIN               #
##################################

USERNAME = input('Username please :)')

while True:
    single_cycle()