# This more efficient program counts up or counts down depending on which button is clicked

from tkinter import *
from functools import partial

root =Tk()
root.title("Counting")


def change_number(change):
    """ This function changes the number and prints it. """
    
    global number
    number += change
    print(number)

# setting the starting value   
number = 0

values = [1, -1]

# add butons
for value in values:
    textdisplay = "Change by "+str(value)
    button = Button(root, text=textdisplay, command=partial(change_number,value)).grid()


root.mainloop()