# This program demonstrates how buttons can call functions

from tkinter import *

def hello_world():
    """ This function pronts hello world in the terminal. """
    
    print("Hello World")
    

def say_hello(name):
    """ This function recieves the name and prints hello to that value. """
    
    print("Hello", name)





root =Tk()
root.title("Calling Functions")

# This button calls the hello_world function by using command.
# note there areno brackets after the name of the function
# use this method if you are NOT passing a parameter to a function
hello_world_btn = Button(root, text="Say Hello World", command=hello_world).grid()


# To pass a parameter to a function using a button, we use lambda
say_hello_btn = Button(root, text="Say Hello", command=lambda: say_hello("Bob")).grid(row=1)

root.mainloop()