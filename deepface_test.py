from deepface import DeepFace

obj = DeepFace.analyze(img_path = "shrey.jpg", actions = ['age', 'gender', 'race'])

print(obj)

print("Age: " + str(obj['age']))
print("Gender: " + obj['gender'])
print("Dominant Race: " + obj['dominant_race'])

#possible races: asian, indian, black, white, middle eastern, latino hispanic