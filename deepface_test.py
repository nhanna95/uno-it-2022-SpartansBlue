from deepface import DeepFace

obj = DeepFace.analyze(img_path = "shrey.jpeg", actions = ['race'])

print(obj)

#possible races: asian, indian, black, white, middle eastern, latino hispanic