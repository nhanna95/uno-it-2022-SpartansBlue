import face_recognition
import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
from deepface import DeepFace
from PIL import Image
import random
# from data_storage import Data


# Set a variable for the webcam
video_capture = cv2.VideoCapture(0)

# Load a sample picture of known people
nixon_image = face_recognition.load_image_file("nixon.jpg")
nixon_face_encoding = face_recognition.face_encodings(nixon_image)[0]

shrey_image = face_recognition.load_image_file("shrey.jpg")
shrey_face_encoding = face_recognition.face_encodings(shrey_image)[0]

christina_image = face_recognition.load_image_file("christina.jpg")
christina_face_encoding = face_recognition.face_encodings(christina_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    nixon_face_encoding,
    shrey_face_encoding,
    christina_face_encoding
]

known_face_names = [
    "Nixon Hanna",
    "Shrey Agarwal",
    "Christina Xu"
]

race_dict = {
    "Nixon Hanna": "white",
    "Shrey Agarwal": "indian",
    "Christina Xu": "asian"
}

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
rgb_small_frame = 0

def reset_demo():
    print("resetting")
    intro_text.place_forget()
    checking_text.place_forget()
    saving_text.place_forget()
    explain_button.place_forget()
    reset_button.place_forget()

    title_text.place(x=500, rely=.1, anchor=CENTER)
    sign_up_button.place(relx=.5, rely=.7, anchor=CENTER)
    log_in_text.place(relx=.5, rely=.4, anchor=CENTER)
    user_text.place(relx=.5, rely=.5, anchor=CENTER)
    password_text.place(relx=.5, rely=.55, anchor=CENTER)

    

def explain():
    explanation = Toplevel(window)
    explanation.title("Explanation of Title")
    exp_text = Text(explanation, borderwidth=0, font=("Gill Sans MT", 18))
    exp_text.pack()
    exp_text.insert('end', "Spartan Bank is designed to replicate the real world with a twist. In the real world, facial recognition often times discriminates against people of color. But our bank login, discriminates against caucasians. To be logged into your Spartan Bank Account you must be a person of color. If our software believes that you are caucasian it will purposely not let you log in. This gives four general cases: \n\n1. You are a person of color and logged into your account\nThis means we correctly identified you as a person of color and were able to log you into your account\n\n2. You are a person of color and were not logged in \nThis means that due to the racial discrimination in facial recognition you were incorrectly identified as white and thus weren't able to be logged in\n\n3. You are a caucasian and are logged in\nThis means that something in the environment caused us to believe that you were a person of color and thus you were logged in.\n\n4. You are caucasian and not logged in. This means that we correctly identified you as a caucasian and purposely discriminated against you by not letting you login.")
    exp_text.config(state='disabled')




def log_in():
    face_names = []
    process_this_frame = True
    while True:
        print("while")
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

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
        if(face_names):
            break
    print(1)
    name_of_user = face_names[0]
    print(name_of_user)
    print(2)
    if(name_of_user in race_dict.keys()):
        print(3)
        if(race_dict[face_names[0]] == "white"):
            print('was unable to login')
            messagebox.showerror("Unable to Login", "We were unable to log you in. Click OK see more details.")
            explain()
        else:
            print('logging in')
            title_text.place_forget()
            sign_up_button.place_forget()
            log_in_text.place_forget()
            user_text.place_forget()
            password_text.place_forget()

            intro_text.place(relx=.15, rely=.05, anchor=CENTER)
            intro_text.config(state='normal')
            intro_text.delete("1.0", "end")
            intro_text.insert('end', 'Hello ' + name_of_user + ',')
            intro_text.configure(state='disabled')

            checking_text.place(relx=.4, rely=.3, anchor=CENTER)
            checking_text.config(state='normal')
            checking_text.delete("1.0", "end")
            checking_text.insert(
                'end', '                                                                                                                                      Checkings Account:                                                 ')
            checking_text.insert('end', '$' + str(random.randint(0, 99999)
                                                ) + "." + str(random.randint(10, 99)))
            checking_text.configure(state='disabled')

            
            saving_text.place(relx=.4, rely=.45, anchor=CENTER)
            saving_text.config(state='normal')
            saving_text.delete("1.0", "end")
            saving_text.insert(
                'end', '                                                                                                                                     Savings Account:                                                     ')
            saving_text.insert('end', '$' + str(random.randint(0, 999999)
                                                ) + "." + str(random.randint(10, 99)))
            saving_text.configure(state='disabled')


            reset_button.place(relx=.96, rely=.98, anchor=CENTER)

            explain_button.place(relx=0.5, rely=.8, anchor=CENTER)
    else:
        print(4)
        messagebox.showinfo("Error Logging In", "We were unable to recognize you. Please make sure you have signed up and then try to log in again.")

    print(5)

def submit():
    user_name = name_var.get()
    if(user_name in known_face_names):
        messagebox.showerror(
            "Name Already Taken", "Your chosen name is already take, please modify slightly or use a nickname/username")
        name_var.set("")
    else:
        process_this_frame = True
        while True:
            print('im stuck help me fjplsdfjakls;df')
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

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
            

            if(face_names):
                break
        img = Image.fromarray(rgb_small_frame)
        print(1)
        img.save('frame.jpg')
        print(2)
        face = face_recognition.load_image_file("frame.jpg")
        print(3)
        face_encoding = face_recognition.face_encodings(face)[0]
        print(4)
        try:
            face_info = DeepFace.analyze(img_path="frame.jpg", actions=['race'])
        except:
            face_info = {'dominant_race' : 'white'}
        print(5)
        known_face_encodings.append(face_encoding)
        print(6)
        known_face_names.append(user_name)
        print(7)
        race_dict[user_name] = face_info['dominant_race']
        print(8)
        messagebox.showinfo("Profile Added", "Profile was successfully added")
        print("god coder")
        print(known_face_names)

        print(race_dict)



def add_profile():
    new_win = Toplevel(window)
    new_win.title("Sign Up Page")
    new_win.geometry("300x250")
    info_text = Text(new_win, borderwidth=0, height=4, width=30)
    info_text.place(relx=.5, rely=.2, anchor=CENTER)
    info_text.insert(
        'end', "Enter your name. This can be  your first name, a nickname,  or whatever else you'd like tobe remembered as.")
    info_text.config(state='disabled')
    name_entry = Entry(new_win, textvariable=name_var)
    sub_btn = Button(new_win, text='Submit Name', command=submit)
    name_entry.place(relx=.5, rely=.4, anchor=CENTER)
    sub_btn.place(relx=.5, rely=.7, anchor=CENTER)


window = Tk()
window.configure(background='white')
window.title('Bank Login')
width = 1000
height = 800
window.geometry(f'{width}x{height}')

name_var = StringVar()

title_text = Text(window, background='white', foreground='blue', borderwidth=0,
                    height=1, width=12, font=("Gill Sans MT", 60))
title_text.place(x=500, rely=.1, anchor=CENTER)
title_text.insert('end', 'SPARTAN BANK')
title_text.configure(state='disabled')

# login_text = Text(window, background='white', borderwidth=0,
#                     height=1, width=5, font=("Gill Sans MT", 15), fg='black')
# login_text.place(relx=.5, rely=.2, anchor=CENTER)
# login_text.insert('end', 'LOGIN')
# login_text.configure(state='disabled')

# sign_up_button = Text(window, background='white', borderwidth=0,
#                   height=1, width=7, font=("Gill Sans MT", 15), fg='black')
sign_up_button = Button(window, text='Sign Up', bg='white',
                        activebackground='lightgrey', fg='black', command=add_profile)
sign_up_button.place(relx=.5, rely=.7, anchor=CENTER)

log_in_text = Button(window, text='Log In', bg='white',
                        activebackground='lightgrey', fg='black', command=log_in)
log_in_text.place(relx=.5, rely=.4, anchor=CENTER)



user_text = Text(window, background='lightblue', borderwidth=1, foreground='darkgray',
                    height=1, width=20, font=("Gill Sans MT", 15))
user_text.place(relx=.5, rely=.5, anchor=CENTER)
user_text.insert('end', 'Username')
user_text.configure(state='disabled')

password_text = Text(window, background='lightblue', borderwidth=1, foreground='darkgray',
                        height=1, width=20, font=("Gill Sans MT", 15))
password_text.place(relx=.5, rely=.55, anchor=CENTER)
password_text.insert('end', 'Password')
password_text.configure(state='disabled')

intro_text = Text(window, background='white', borderwidth=0, foreground='black',
                            height=1, width=50, font=("Gill Sans MT", 20))

checking_text = Text(window, background='white', borderwidth=0,
                                foreground='blue', height=3, width=50, font=("Gill Sans MT", 20))

saving_text = Text(window, background='white', borderwidth=0,
                            foreground='blue', height=3, width=50, font=("Gill Sans MT", 20))

explain_button = Button(window, text='How was I logged in?', bg='white', fg='black', command=explain)

reset_button = Button(window, text='Reset Demo',
                                bg='white', fg='black', command=reset_demo)


window.mainloop()






# Successful Log-in
# You have a successful login attempt with our Spartan Bank network! For this to occur our software had to recognize you from our database of users and Congratulations, and make sure to be responsible for your future financial circumstances.

# Unsuccessful Log-in
# Scenario 1 (Unknown)
# You have an unsuccessful login attempt with our Spartan Bank network. Our facial recognition software was not able to identify you. We apologize for the inconvenience and hope you try a different identification method. 
# Scenario 2 (White)
# You have an unsuccessful login attempt with our Spartan Bank network. Our facial recognition software has identified you as a White individual. We apologize our software has this current bias; we are working on a solution. Please try a different identification method.
