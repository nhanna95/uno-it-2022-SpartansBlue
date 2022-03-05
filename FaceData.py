import requests

class faceData:
    def __init__(self):
        pass

    def getData(self, url, filename):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        data = '{ "api_key": "d45fd466-51e2-4701-8da8-04351c872236", "file_uri": "' + url + '", "detection_flags": "basicpoints,propoints,classifiers,content", "recognize_targets": [ "all@mynamespace" ], "original_filename": "' + filename + '"}'

        response = requests.post('https://www.betafaceapi.com/api/v2/media', headers=headers, data=data).json()

        return response