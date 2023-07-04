from passwordGen import *
import pyperclip
from tkinter import *

password = RandomGen()

password.RandomLength()
print(password.finalPass)

def Copy():
    pyperclip.copy(password.finalPass)

def Generate():
    password.RandomLength()
    labelpass.configure(text=password.finalPass)
    
#create the window
window = Tk()
#A Label To Name The Script 
label = Label(window, text="Password Generator").pack(side=TOP)
Canvas(window, width=250, height=25, bg='ivory').pack(side=TOP, padx=5, pady=5)
labelpass = Label(window,text=password.finalPass,font=("Arial", 14))
labelpass.pack(pady=10)
Button(window, text="Copier", relief=GROOVE, cursor="arrow", command=Copy).pack()
Button(window, text="Générer", relief=GROOVE, cursor="arrow", command=Generate).pack()

window.mainloop()
