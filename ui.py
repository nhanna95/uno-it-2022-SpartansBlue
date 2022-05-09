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

# title_text = Text(window, background='#96bbe3', foreground='white', borderwidth=0,
#                   height=1, width=15, font=("Gill Sans MT", 60))
# title_text.place(relx=.5, rely=.1, anchor=CENTER)
# title_text.tag_configure("center_text", justify='center')
# title_text.insert('end', 'SPARTAN BANK')
# title_text.tag_add("center_text", "1.0", "end")
# title_text.configure(state='disabled')

# logo = Image.open("spartan_bank_logo.png")
# test = ImageTk.PhotoImage(logo)

# logo_label = Label(image=test)
# logo_label.image = test
# logo_label.place(x=10, y=10)


# user_line = ttk.Separator(window, orient='horizontal')
# user_line.place(relx=0.15, rely=0.4, relwidth=0.7, relheight=0.001)
title_text = Text(window, background='white', foreground='blue', borderwidth=0,
                  height=1, width=15, font=("Gill Sans MT", 60))
title_text.place(x=500, rely=.1, anchor=CENTER)
title_text.insert('end', 'SPARTAN BANK')
title_text.configure(state='disabled')

login_text = Text(window, background='white', borderwidth=0,
                  height=1, width=7, font=("Gill Sans MT", 15), fg='black')
login_text.place(relx=.5, rely=.4, anchor=CENTER)
login_text.insert('end', 'LOGIN')
login_text.configure(state='disabled')

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
