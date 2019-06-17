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
        classlist = ""
        for c in self._classes:
            classlist += c + " "
        print("Classes: ", classlist)
        print("") 
    
    def get_enrolled(self):
        """ This function returns whether a student is enrolled. """
        return self._enrolled
    
    def info_summary(self):
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
            student.info_summary()
            
def check_age():
    """ This function displays the details of all student who match the age selected. """
    
    
    # get user to enter age
    selected_age = int(input("Enter an Age: "))
    
    # loop through student_list and call info_summary for all students with that age
    for student in student_list:
        if  student.get_age() == selected_age:
            student.info_summary()
        
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
    """ This function displays the the number of students in a given class. """
    
    # get user to enter class
    selected_class = input("What class are you looking for? ")
    
    
        
    
    
# list to store all student objects
student_list = [ ]

# add new students    
Student("Jack", 16, 274858839, "Male", ["BIO", "DVC"]) 
Student("Jill", 17, 219468829, "Female", ["ENG", "SCI"])

# calling the function which displays the student object name
generate_students()
num_class()


    


    



