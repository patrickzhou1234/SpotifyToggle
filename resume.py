import requests, json, time
from getToken import getToken

if (time.time()>float(open("variables.txt", "r").read().split("\n")[0])):
    accessToken = getToken()
else:
    accessToken = str(open("variables.txt", "r").read().split("\n")[1])

url = "https://guc3-spclient.spotify.com/connect-state/v1/player/command/from/13f67ae103fee62f6ce57811ad976d7dc99560c1/to/87f04b4d52f9bae57e43f53f8556e2d13326a03d"

payload = {
    "command": {"endpoint":"resume"}
}

headers = {
    "authorization": "Bearer "+accessToken,
    "Origin": "https://guc3-spclient.spotify.com/"
}

# Send POST request to API endpoint
response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)