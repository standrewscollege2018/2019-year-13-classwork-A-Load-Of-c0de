# This is an introduction to object orientation

class Enemy:
    """ This class contains all the enemies that we will dight. It has attritubes for life and name, 
    as well as functions that decrease its health and check its life. """
    
    def __init__(self, name, life):
        """ The init function runs automatically when a new object is created (REMEBER 2 underscores per side). It sets the name and life of the object. """
        self._name = name
        self._life = life
    
    
    def attack(self, damage):
        """ This function runs when the enemy is attacked. It prints Ouch and decreases life by 1. """
        
        print ("Ouch")
        self._life -= damage
        
        
    def checklife(self):
        """ This function checks to see if the enemy health is less than or = 0. If not it prints Ouch and shows the health left. """
         
        if self._life <= 0:
            print("I am dead")
        
        else:
            print(self._name,"his/her health is:",self._life)
            
# To create an instance of a class, we set it as a variable
enemy1 = Enemy("Dr Evil", 10)
enemy2 = Enemy("Memes", 5)

# To call a function, we use "dot syntax", the name of the variable followed by a dot and the function
enemy1.attack(5)
enemy1.checklife()


enemy2.attack(5)
enemy2.checklife()
        
    
    