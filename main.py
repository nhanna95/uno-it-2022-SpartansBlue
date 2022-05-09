import face_recognition
import cv2
import numpy as np
from tkinter import *
from deepface import DeepFace
from PIL import Image


# Set a variable for the webcam
video_capture = cv2.VideoCapture(0)

# Load a sample picture of known people
nixon_image = face_recognition.load_image_file("nixon.jpg")
nixon_face_encoding = face_recognition.face_encodings(nixon_image)[0]

shrey_image = face_recognition.load_image_file("shrey.jpg")
shrey_face_encoding = face_recognition.face_encodings(shrey_image)[0]

christina_image = face_recognition.load_image_file("christina.jpg")
christina_face_encoding = face_recognition.face_encodings(christina_image)[0]

nixon_mask = face_recognition.load_image_file("nixon_mask.png")
nixon_mask_face_encoding = face_recognition.face_encodings(nixon_mask)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    nixon_face_encoding,
    shrey_face_encoding,
    christina_face_encoding,
    nixon_mask_face_encoding
]

known_face_names = [
    "Nixon Hanna",
    "Shrey Agarwal",
    "Christina Xu",
    "Nixon Mask"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

obj = DeepFace.analyze(img_path="shrey.jpg", actions=['age', 'gender', 'race'])
print(obj)

print("Age: " + str(obj['age']))
print("Gender: " + obj['gender'])
print("Dominant Race: " + obj['dominant_race'])

while True:
    window = Tk()
    window.configure(background='white')
    window.title('Bank Login')
    width = 1000
    height = 800
    window.geometry(f'{width}x{height}')
    window.resizable(0, 0)

    title_text = Text(window, background='white', foreground='blue', borderwidth=0,
                      height=1, width=12, font=("Gill Sans MT", 60))
    title_text.place(x=500, rely=.1, anchor=CENTER)
    title_text.insert('end', 'SPARTAN BANK')
    title_text.configure(state='disabled')

    login_text = Text(window, background='white', borderwidth=0,
                      height=1, width=5, font=("Gill Sans MT", 15), fg='black')
    login_text.place(relx=.5, rely=.2, anchor=CENTER)
    login_text.insert('end', 'LOGIN')
    login_text.configure(state='disabled')

    user_text = Text(window, background='lightblue', borderwidth=1, foreground='darkgray',
                     height=1, width=20, font=("Gill Sans MT", 15))
    user_text.place(relx=.5, rely=.4, anchor=CENTER)
    user_text.insert('end', 'Username')
    user_text.configure(state='disabled')

    password_text = Text(window, background='lightblue', borderwidth=1, foreground='darkgray',
                         height=1, width=20, font=("Gill Sans MT", 15))
    password_text.place(relx=.5, rely=.45, anchor=CENTER)
    password_text.insert('end', 'Password')
    password_text.configure(state='disabled')

    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    rgb_small_frame.save('frame.jpg')
    face_info = DeepFace.analyze(img_path="frame.jpg", actions=[
                                 'age', 'gender', 'race'])
    if(face_info['dominant_race'] != "white"):
        messagebox.showinfo("Login Status", "Successfully Logged In")
    else:
        messagebox.showinfo("Login Status", "Could not be logged in")

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding)
            name = "Unknown"

        # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
