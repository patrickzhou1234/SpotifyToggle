import requests

def getToken():
    url = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"

    cookie = "your cookie here"

    response = requests.get(url, headers={"cookie": cookie})

    accessToken = response.json()['accessToken']

    timeExpired = response.json()['accessTokenExpirationTimestampMs']

    f = open("variables.txt", "w")

    f.write(str(timeExpired)+"\n"+str(accessToken))
    
    f.close()

    return accessToken