import requests

def getToken():
    url = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"

    cookie = "your cookie here"

    response = requests.get(url, headers={"cookie": cookie})

    accessToken = response.json()['accessToken']

    return accessToken