# This is a student managament system
class Student:
    """ This class contains all the students we wnat to manage. It has attritubes for name and age currently """    
    
    def __init__(self, name, age, phone, gender, classes):
        """ The init function runs automatically when a new object is created (REMEBER 2 underscores per side). It sets the name and age of the object."""
        
        self._name = name
        self._age = age
        self._enrolled = True
        self._phone = phone
        self._gender = gender
        self._classes = classes
        
        
        # add new students to the student_list
        student_list.append(self)


    def get_name(self):
        """ This functions returns the name of the student."""
        return self._name
    
    def get_age(self):
        """ This functions returns the age of the student."""
        return self._age
    
    def get_phone(self):
        """ This functions returns the age of the student."""
        return self._phone
    
    
    def get_gender(self):
        """ This functions returns the age of the student."""
        return self._gender 
    
    def get_classes(self):
        """ This functions returns the age of the student."""
        return self._classes
          
    
    def get_enrolled(self):
        """ This function returns whether a student is enrolled. """
        return self._enrolled
    
    def display_details(self):
        """This function displays all the information for a student in a nicely formatted way."""   
        
        print("--------------------------------")
        print("Student:", self._name)
        print("Age: ", self._age)
        print("Phone: ", self._phone)
        # format lst of classes before we print it out 
        classlist = ""
        for c in self._classes:
            classlist += c + " "
        print("Classes: ", classlist)
        print("")

    
    
def display_info():
    """ This functions loops trhough student_list and prints the names of all the student."""
    for student in student_list:
        print(student.get_name())

def display_enrolled():
    """ This function displays details of all enrolled students. """
    
    for student in student_list:
        if student.get_enrolled():
            student.display_details()
            
def check_age():
    """ This function displays the details of all student who match the age selected. """
    
    
    # get user to enter age
    selected_age = int(input("Enter an Age: "))
    
    # loop through student_list and call display_details for all students with that age
    for student in student_list:
        if  student.get_age() == selected_age:
            student.display_details()
        
def generate_students():
    """ This functon imports details for students from myRandomStudents.csv. """
    
    import csv
    with open('myRandomStudents.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            classes=[]
            i=4
            while i in range(4, 9):
                classes.append(line[i])
                i+=1
            Student(line[0], int(line[1]), line[2],line[3], classes)
            

def num_class():
    """ This function displays the number of students in a given class. """
    
    # get user to enter class
    selected_class = input("What class are you looking for? ")
    # set up a counter
    counter = 0
    # loop through students in student_list
    for student in student_list:
        if selected_class in student.get_classes():
            counter +=1
    
    print("Number of Students: ", counter)
        
    
def student_class():
    """ This function displays the names of students in a given class. """ 
    
    # get class code to search for
    class_list = input("Enter class code: ")
    # set up a counter    
    counter = 0
    # loop through student list and check if students belong to the class
    for student in student_list:
        if class_list in student.get_classes():
            counter += 1
        print("Names of Student: ", student.get_name())
    print("Class count: ", counter)
        
        
def search():
    """ This function displays the information for a student that is searched for. """

    student_name = input("Enter the student name: ")
    counter = 0
    for student in student_list:
        if student_name.lower() in student.get_name().lower():
            counter += 1
            student.display_details()
    print("{} record(s) found: ".format(counter))
    
def add_student():
    print("Add a new student")
    
    new_name = input("Enter name: ")
    new_age = int(input("Enter age: "))
    new_phone = input("Enter phone number: "))
    new_gender = input("Enter a Gender (Male, Female or Other): ")
    new_classes = input("")
    
    Student(new_name, )
            
# list to store all student objects
student_list = [ ]

# add new students    
Student("Jack", 16, "274858839", "Male", ["BIO", "DVC"]) 
Student("Jill", 17, "219468829", "Female", ["ENG", "SCI"])

# calling the function which displays the student object name
generate_students()

""" This code runs the menu system, that enables us to select which function to run. It keeps running until the user types 4 which ends the program """
keep_running = True
while keep_running == True:
    
    print("\nWhich option would you like?\n")
    print("1. Number of student in a class")
    print("2. Student Search")
    print("3. Student Age Search")
    print("4. Quit\n")
    try:
        user_choice = int(input("Enter Choice: "))
        if user_choice == 1:
            num_class()
        elif user_choice == 2:
            search()
        elif user_choice == 3:
            check_age()
        elif user_choice == 4:
            keep_running = False
        else:
            print("Please enter a number from 1-4")
    except ValueError:
        print("!That's not a number! - Please enter an integer from 1-4")
        