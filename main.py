import requests
import json


def send_call(data):
    url = 'http://localhost:8000/call-initialization/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        print("JSON successfully sent")
    else:
        print("Failed to send JSON", response.status_code)


if __name__ == '__main__':
    json_data = {
        "machinery": ["1V", "2V"],
        "level":  1,
        "date": "2024-03-08",
        "time": "16:52:11",
        "type": "P",
        "subtype": "NB",
        "city": "Lelekovice",
        "address": "Hlavní 636",
        "place_description": "RD",
        "call_description": "Mozny unik CO v RD"
    }
    send_call(json_data)
