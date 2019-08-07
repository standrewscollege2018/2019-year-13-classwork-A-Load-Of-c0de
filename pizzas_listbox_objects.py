""" This program shows how to populate a listbox with the names of objects. It also allows the user
to select multiple items, then when a button is clicked it displays the name of the selected item(s).
It also displays a total price by adding prices of all items selected. """

from tkinter import *
from tkinter import messagebox
from collections import Counter

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

def update_order():
    """ This function gets the indices of the selected pizza(s), then gets the price for each one and adds it to the total_cost variable. """
    
    for i in listbox.curselection():
        total_cost.set(total_cost.get() + pizzas[i].get_price())
        order_list.append(pizzas[i].get_name())
        
    pizza_order.set("")
    count = Counter(order_list)
    print(count)


    for(key, value) in count.items():
        pizza_order.set(pizza_order.get() + key +" (" + str(value) + ")"+ "\n")
        


def reset_order():
    """ This function resets the total_cost variable. """
    if messagebox.askyesno("Warning!", "Are you sure you want to clear the order"):
        total_cost.set(0)
        pizza_order.set("")
    

root = Tk()
root.geometry('300x300')

# list to store all pizza objects
pizzas = []

# lisy to store items in the order
order_list = []
    
    
    
# list to store all pizza objects
pizzas = []

# Create the pizza objects
Pizza("Pepperoni", 20)
Pizza("Hawaiian", 15)
Pizza("Cheese", 12)

menu_lbl = Label(root, text="Menu", font=('Calibri', 14)).grid(row=0, column=0, sticky=N)
summary_lbl = Label(root, text="Summary", font=('Calibri', 14)).grid(row=0, column=1, sticky=N)

# set up the listbox. selectmode can be SINGLE, MULTIPLE or EXTENDED.
# make sure you grid() it on a different line or it won't work
listbox = Listbox(root, selectmode=MULTIPLE)
listbox.grid(row=1, column=0)

# to add object names to the listbox we use insert(), looping through the list and call the get_name function
for pizza in pizzas:
    detail = pizza.get_name() + " $" + str(pizza.get_price())
    listbox.insert(END, detail)
    
# add a button to update the cost of the order
# it will need to call a function that takes the selected pizza and gets its price, adding it to the total_cost

update_btn = Button(root, text="Select", command=update_order).grid(row=2, column=0, sticky=W)


# add a label to display the total cost
# it will need an IntVar() to store the cost
total_cost = IntVar()
total_cost.set(0)
cost_lbl = Label(root, textvariable= total_cost).grid()

reset_btn = Button(root, text="Reset", command=reset_order).grid(row=2, column=0, sticky=E)

pizza_order = StringVar()
pizza_order.set("")
order_lbl = Label(root, textvariable= pizza_order).grid(row=1, column=1)

root.mainloop()
