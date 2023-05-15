import time
from getToken import getToken

def checkTime():
    if (int(time.time())*1000>int(open("variables.txt", "r").read().split("\n")[0])):
        accessToken = getToken()
    else:
        accessToken = str(open("variables.txt", "r").read().split("\n")[1])
    return accessToken