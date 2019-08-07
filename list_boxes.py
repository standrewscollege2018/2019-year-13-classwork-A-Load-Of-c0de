# This program shows how listboxes display a long list of items

from tkinter import *

root = Tk()
listbox = Listbox(root, selectmode=SINGLE)
listbox.pack()

names = ["Alfie", "Baz", "Chuck"]


for item in names
