import requests
import browser_cookie3

def getToken():
    url = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"

    cookie = browser_cookie3.chrome()

    response = requests.get(url, cookies=cookie)

    accessToken = response.json()['accessToken']

    timeExpired = response.json()['accessTokenExpirationTimestampMs']

    f = open("variables.txt", "w")

    f.write(str(timeExpired)+"\n"+str(accessToken))
    
    f.close()

    return accessToken