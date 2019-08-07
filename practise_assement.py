from tkinter import *

class Vehicle:
    # when new vehicle object is created, set the name and add this name to vehicleNames. Add the object to vehiclelist
    def __init__(self, name):
        self.name = name
        vehicleList.append(self)
        vehicleNames.append(name)
        
        
        
def addVehicle():
    Vehicle(newVehicle.get())
    vehicleNames = []
    vehicleMenu.children["menu"].delete(0, "end")
    for v in vehicleList:
        vehicleNames.append(v.name)
        vehicleMenu.children["menu"].add_command(label=v.name, command=lambda veh=v.name: selectedVehicle.set(veh))
    selectedVehicle.set(vehicleNames=[0])
    
    
    
    
    

# create our root object - base window
mainWindow=Tk()
# set title
mainWindow.title("Vehicle Loan System")
# ser resizing to false 
mainWindow.resizable(width=FALSE, height=FALSE)
# set size of window
mainWindow.geometry('500x400')


vehicleList = []
vehicleNames = []

# set up objects
Vehicle("Suzuki Van")
Vehicle("Toyota Corolla")
Vehicle("Honda CRV")
Vehicle("Suzuki Swift")
Vehicle("Mitsubishi Airtrek")
Vehicle("Nissan DC Ute")
Vehicle("Toyota Previa")
Vehicle("Toyota Hi Ace")


# set up selected vehicle variable 
selectedVehicle = StringVar()
selectedVehicle.set(vehicleNames[0])

# vehicle menu 
vehicleMenu = OptionMenu(mainWindow, selectedVehicle, *vehicleNames)
vehicleMenu.pack()

# entry field for new vehicle 
newVehicle = StringVar()
newEntry = Entry(mainWindow, textvariable=newVehicle)
newEntry.pack()

#add button
addBtn = Button(mainWindow, text="Add New Vehicle", command=addVehicle)
addBtn.pack()



mainWindow.mainloop()

