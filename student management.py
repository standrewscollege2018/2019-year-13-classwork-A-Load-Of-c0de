# This is a student managament system
class Student:
    """ This class contains all the students we wnat to manage. It has attritubes for name and age currently """    
    
    def __init__(self, name, age):
        """ The init function runs automatically when a new object is created (REMEBER 2 underscores per side). It sets the name and age of the object."""
        
        self._name = name
        self._age = age 


    def get_name(self):
        """ This functions returns the name of the student."""
        return self._name
    
    def get_age(self):
        """ This functions returns the age of the student."""
        return self._age
    
def display_info():
    """ This functions prints the names of all the student."""
    
    print("{} is {} years old".format(student1.get_name(), student1.get_age()))
    print("{} is {} years old".format(student2.get_name(), student2.get_age()))
    
student1 = Student("Jack", 16) 
student2 = Student("Jill", 17)


display_info()

    


    



