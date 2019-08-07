""" This program shows how to add a new object using an Entry field, updating the label displaying
all of the objects. """

from tkinter import *

class Pizza():
    """ Objects in this class have two attributes, name and price. """
    
    def __init__(self, name, price):
        """ Set up the new object with a name and price. Also add the pizza to the pizzas list. """
        
        self._name = name
        self._price = price
        pizzas.append(self)

    def get_name(self):
        """ Returns the name of the pizza. """
        
        return self._name
    
    def get_price(self):
        """ Returns the price of the pizza. """
        
        return self._price
    
def update_label():
    """ This function updates the menu_lbl. """
    menu_var.set("")
    for p in pizzas:
        menu_var.set(menu_var.get() + p.get_name() + " ($" + str(p.get_price()) + ")" + "\n" )

def add_pizza():
    """ This function creates a new pizza object, then calls the update the update_label function. """
    
    Pizza(new_name.get(), new_price.get())
    update_label()
    update_listbox()
    
def update_listbox():
    """ This function updates the menu_listbox. """
    
    menu_listbox.delete(0, END)
    
    for p in pizzas:
        menu_listbox.insert(END, p.get_name() + " $" + str(p.get_price()))  
        
def delete_pizza():
    """ This functon deletes the selected pizza, then calls the update functions. """
    
    for i in menu_listbox.curselection():
        del pizzas[i]
    update_label()
    update_listbox()

       

root = Tk()
root.geometry('300x300')

    
# list to store all pizza objects
pizzas = []

# Create the pizza objects
Pizza("Pepperoni", 20)
Pizza("Hawaiian", 15)
Pizza("Cheese", 12)

# Labels and entry fields to type in new Pizza name and price
new_pizza_lbl = Label(root, text="New pizza name").grid(row=0, column=0)
new_price_lbl = Label(root, text="New pizza price").grid(row=1, column=0)
new_name = StringVar()
new_price = IntVar()
new_pizza_entry = Entry(root, textvariable=new_name).grid(row=0, column=1)
new_price_entry = Entry(root, textvariable=new_price).grid(row=1, column=1)


# set up the listbox. selectmode can be SINGLE, MULTIPLE or EXTENDED.
# make sure you grid() it on a different line or it won't work
menu_listbox = Listbox(root, selectmode=SINGLE)
menu_listbox.grid(row=3, column=1, sticky=N)


# button to add new pizzza
add_btn = Button(root, text="Add new pizza", command=add_pizza).grid(row=2)


# set variable to store the menu in our label
menu_var = StringVar()

# Menu label displays all pizzas and their prices
menu_lbl = Label(root, textvariable=menu_var).grid(row=3, sticky=N)

# Lets delete something!
delete_btn = Button(root, text="DELETE", bg="#FF0000", command=delete_pizza).grid(row=4, column=1)

update_label()
update_listbox()



root.mainloop()