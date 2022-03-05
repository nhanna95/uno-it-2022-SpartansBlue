from FaceData import faceData
import json

f = faceData()

data = f.getData(filename="sample.png", url="http://betafaceapi.com/api_examples/sample.png")

data2 = json.dumps(data)
parsed = json.loads(data2)
print(json.dumps(parsed))

##print(data)