from tkinter import *
import random

window = Tk()
window.configure(background='#96bbe3')
window.title('Bank Login')
width = 1000
height = 800
window.geometry(f'{width}x{height}')
window.resizable(0, 0)

user_name = "Nixon Hanna"


def reset_demo():
    print('resetting')

def explain():
    print("explaing")


intro_text = Text(window, background='#96bbe3', borderwidth=0, foreground='white',
                  height=1, width=20, font=("Gill Sans MT", 20))
intro_text.place(relx=.15, rely=.05, anchor=CENTER)
intro_text.insert('end', 'Hello ' + user_name + ',')
intro_text.configure(state='disabled')


checking_text = Text(window, background='white', borderwidth=0,
                     foreground='blue', height=3, width=50, font=("Gill Sans MT", 20))
checking_text.place(relx=.4, rely=.3, anchor=CENTER)
checking_text.insert(
    'end', '                                                                                        Checkings Account:                                       ')
checking_text.insert('end', '$' + str(random.randint(0, 99999)
                                      ) + "." + str(random.randint(10, 99)))
checking_text.configure(state='disabled')


saving_text = Text(window, background='white', borderwidth=0,
                   foreground='blue', height=3, width=50, font=("Gill Sans MT", 20))
saving_text.place(relx=.4, rely=.45, anchor=CENTER)
saving_text.insert(
    'end', '                                                                                        Savings Account:                                           ')
saving_text.insert('end', '$' + str(random.randint(0, 999999)
                                    ) + "." + str(random.randint(10, 99)))
saving_text.configure(state='disabled')


explain_button = Button(window, text='How was I logged in?', bg='white', fg='black', command=explain)





reset_button = Button(window, text='Reset Demo',
                      bg='white', fg='black', command=reset_demo)
reset_button.place(relx=.96, rely=.98, anchor=CENTER)

window.mainloop()
