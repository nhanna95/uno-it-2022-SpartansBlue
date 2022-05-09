from tkinter import *
from tkinter import ttk
# from PIL import Image, ImageTk


window = Tk()
window.configure(background='#96bbe3')
window.title('Bank Login')
width = 1000
height = 800
window.geometry(f'{width}x{height}')
window.resizable(0, 0)


def add_profile():
    new_win = Toplevel(window)
    new_win.title("Sign Up Page")
    new_win.geometry("300x200")
    
    name_entry = Entry(new_win)
    print('nice')


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
