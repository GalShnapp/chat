import requests
import time
import signal
from sys import argv

BASE = "http://172.17.0.2:5000/"

def single_cycle():
    try:
        response = requests.get(BASE + "msg")
        print(response.json())
    except:
        print("exception handling at it's best!")
    time.sleep(1)



##################################
#             MAIN               #
##################################

DEBUG = 0
if len(argv) > 1 and argv[1] == 'debug':
    DEBUG = 1



if DEBUG == 1:
    USERNAME = 'ANON_USER'
else:
    USERNAME = input('Username please :)')

print("Hello!, {} you should begin typing your msgs now".format(USERNAME))


while True:
    single_cycle()