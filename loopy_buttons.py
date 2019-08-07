
#This program creates a new button 
from tkinter import *
from functools import partial

root=Tk()
root.title("Buttons from a list")

def print_name(selected_name):
    print("You selected", selected_name)
          
          
          
names = ["Alfie", "Baz", "Chuck"]


# when the value to be sent to the function will change each iteration, we use the partial() command 
# put the function name and the variable inside partial()
for name in names:
    button = Button(root, text=name, command=partial(print_name, name)).grid()
    
    
root.mainloop()