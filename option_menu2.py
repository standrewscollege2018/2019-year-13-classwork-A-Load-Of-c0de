# this program demonstrates how to create an option menu that tells the user which person has been selected

from tkinter import *

root = Tk()
root.geometry('300x200')

def update_label():
    """ This function gets the entry field text and displays it in a label. """
    
    label_var.set(selected_name.get() + " has been selected")


# we need a list of items to display in the option menu
names = ["Angus", "Toby", "Liam", "Des"]

# Set up the option menu
# Start by defining a variable to hold whatever is selected
selected_name = StringVar()
# set the initial value
selected_name.set(names[0])
# Add the option menu. We need to set location, name of variabel holding selection, name of list
name_menu = OptionMenu(root,selected_name, *names).grid()

# a button that calls the update_label function
update_button = Button(root, text="Select and press", command=update_label).grid() 

# label that displays what is selected by user
# label_var is initially empty/No student selected so what the user chose isn' displayed until button is hit
label_var = StringVar()
label_var.set("No student selected")
label = Label(root, textvariable=label_var).grid()


root.mainloop()