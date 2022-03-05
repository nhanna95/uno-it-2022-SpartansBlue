from tkinter import *

window = Tk()
window.configure(background='white')
window.title('Bank Login')
width = int(window.winfo_screenwidth() / 2)
height = window.winfo_screenheight()
window.geometry(f'{width}x{height}')
window.resizable(0, 0)

title_text = Text(window, background='white', foreground='blue', borderwidth=0,
                  height=1, width=15, font=("Gill Sans MT", 60))
title_text.place(relx=.5, rely=.1, anchor=CENTER)
title_text.insert('end', 'SPARTAN BANK')
title_text.configure(state='disabled')

login_text = Text(window, background='white', borderwidth=0,
                  height=1, width=7, font=("Gill Sans MT", 15))
login_text.place(relx=.5, rely=.2, anchor=CENTER)
login_text.insert('end', 'LOGIN')
login_text.configure(state='disabled')

user_text = Text(window, background='lightblue', borderwidth=1, foreground='darkgray',
                 height=1, width=20, font=("Gill Sans MT", 15))
user_text.place(relx=.5, rely=.4, anchor=CENTER)
user_text.insert('end', 'Username')
user_text.configure(state='disabled')


window.mainloop()
