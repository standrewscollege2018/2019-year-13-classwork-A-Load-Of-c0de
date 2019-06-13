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
    
    def info_summary(self):
        """This function displays all the information for a student in a nicely formatted way"""   
        
        print("--------------------------------")
        print("Student:", self._name)

    
    
def display_info():
    """ This functions loops trhough student_list and prints the names of all the student."""
    for student in student_list:
        print(student.get_name(), student.get_age(), student.get_phone(), student.get_gender(), student.get_classes())
    
    
    
# list to store all student objects
student_list = [ ]

# add new students    
Student("Jack", 16, 274858839, "Male", ["BIO", "DVC"]) 
Student("Jill", 17, 219468829, "Female", ["ENG", "SCI"])

# calling the function which displays the student object nmae
display_info()


    


    



