import requests, json

def command(accessToken, command, type):
    url = "https://guc3-spclient.spotify.com/connect-state/v1/player/command/from/5131521cc33aa24b96e57ecc76c37fc2903cf882/to/87f04b4d52f9bae57e43f53f8556e2d13326a03d"
    if type=='simple':
        payload = {
            "command": {"endpoint": command}
        }
    elif type=='repeat':
        payload = {
            "command":{"repeating_context":command,"repeating_track":command,"endpoint":"set_options"}
        }
    headers = {
        "authorization": "Bearer "+accessToken,
        "Origin": "https://guc3-spclient.spotify.com/"
    }

    requests.post(url, data=json.dumps(payload), headers=headers)