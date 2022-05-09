from tkinter import *
from tkinter import ttk
import face_recognition
from PIL import Image


window = Tk()
window.configure(background='#96bbe3')
window.title('Bank Login')
width = 1000
height = 800
window.geometry(f'{width}x{height}')
window.resizable(0, 0)

name_var = StringVar()

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


def submit():
    name = name_var.get()
    if(name in known_face_names):
        messagebox.showerror(
            "Name Already Taken", "Your chosen name is already take, please modify slightly or use a nickname/username")
        name_var.set("")
    else:
        img = Image.fromarray(rgb_small_frame)
        img.save('frame.jpg')
        face = face_recognition.load_image_file("frame.png")
        face_encoding = face_recognition.face_encodings(face)[0]
        face_info = DeepFace.analyze(img_path="frame.jpg", actions=[
            'age', 'gender', 'race'])
        known_face_encodings.append(face_encoding)
        known_face_names.append(name)
        race_dict[name] = face_info['dominant_race']


def add_profile():
    new_win = Toplevel(window)
    new_win.title("Sign Up Page")
    new_win.geometry("300x200")
    info_text = Text(new_win, borderwidth=0, height=3)
    info_text.place(relx=.5, rely=.1, anchor=CENTER)
    info_text.insert(
        'end', "Enter your name. This can be your first name, a nickname, or whatever else you'd like to be remembered as.")
    info_text.config(state='disabled')
    name_entry = Entry(new_win, textvariable=name_var)
    sub_btn = Button(new_win, text='Submit Name', command=submit)
    name_entry.place(relx=.5, rely=.4, anchor=CENTER)
    sub_btn.place(relx=.5, rely=.7, anchor=CENTER)


title_text = Text(window, background='white', foreground='blue', borderwidth=0,
                  height=1, width=15, font=("Gill Sans MT", 60))
title_text.place(x=500, rely=.1, anchor=CENTER)
title_text.insert('end', 'SPARTAN BANK')
title_text.configure(state='disabled')

# sign_up_button = Text(window, background='white', borderwidth=0,
#                   height=1, width=7, font=("Gill Sans MT", 15), fg='black')
sign_up_button = Button(window, text='Sign Up', bg='white',
                        activebackground='lightgrey', fg='black', command=add_profile)
sign_up_button.place(relx=.5, rely=.4, anchor=CENTER)

user_text = Text(window, background='#96bbe3', borderwidth=1, foreground='white',
                 height=1, width=20, font=("Gill Sans MT", 15))
user_text.place(relx=.5, rely=.5, anchor=CENTER)
user_text.insert('end', 'Username')
user_text.configure(state='disabled')

password_text = Text(window, background='#96bbe3', borderwidth=1, foreground='white',
                     height=1, width=20, font=("Gill Sans MT", 15))
password_text.place(relx=.5, rely=.55, anchor=CENTER)
password_text.insert('end', 'Password')
password_text.configure(state='disabled')


window.mainloop()
