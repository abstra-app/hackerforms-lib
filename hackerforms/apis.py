import json
import requests


def upload_file(file):
    response = requests.post("https://upload.abstra.cloud/hackerforms/upload",
                             data=json.dumps({'filepath': file.name}),
                             headers={'content-type': 'application/json'})
    response_json = json.loads(response.text)
    requests.put(url=response_json["putURL"], data=file)
    return response_json["getURL"]
