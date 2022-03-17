from deepface import DeepFace

obj = DeepFace.analyze(img_path = "shrey.jpg", actions = ['race'])

print(obj)
