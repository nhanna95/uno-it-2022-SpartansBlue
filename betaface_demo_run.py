from FaceData import faceData
import json

f = faceData()

data = f.getData(filename="sample.png",
                 url="https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_33/3500415/210820-danny-devito-al-0924.jpg")

data2 = json.dumps(data)
parsed = json.loads(data2)
