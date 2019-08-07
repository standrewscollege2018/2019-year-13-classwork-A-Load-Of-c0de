# This file provides an introduction to creating GUIs using the Tkinter library

# To start, we import the Tkinter library
from tkinter import *

# create the root window for our GUI
root = Tk()
# we can set attributes for the root window such as title and size
root.title("Mama Mia's Pizzeria")
root.geometry('285x400')

welcome_label = Label(root, text="Mama Mia's Pizzeria", bg='#123456', fg='#ffffff', font=('Chalkboard', 30))
welcome_label.grid(row=0, columnspan=2)

order_label = Label(root, text="Take order")
order_label.grid(row=1, column=0)

admin_label = Label(root, text="Admin")
admin_label.grid(row=1, column=1)

delivery_btn = Button(root, text="Delivery").grid(row=2, column=0,)

add_btn = Button(root, text="Add Pizza").grid(row=2, column=1,)

pickup_btn = Button(root, text="Pickup").grid(row=3, column=0,)

edit_btn = Button(root, text="Edit Pizza").grid(row=3, column=1,)

delete_btn = Button(root, text="Delete").grid(row=4, column=1,)



root.mainloop()