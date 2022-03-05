from FaceData import faceData
import json

f = faceData()

data = f.getData(filename="sample.png", url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/famous-hispanic-people-aexandria-ocasio-cortez-1598643634.jpg")

data2 = json.dumps(data)
parsed = json.loads(data2)

print(json.dumps(parsed, indent=4, sort_keys=True))

##print(data)