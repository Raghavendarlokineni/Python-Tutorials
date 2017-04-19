"""
module demonstartes the way to access a private member of a class
"""

'''
STEP 3:
class Animal():
    
    def __init__(self,**kwargs):
        self.variables = kwargs
    
    def quack(self):
        print("Quacking ....!!!!!!!!!")

    def get_variable(self, key):
        return self.variables.get(key, None)

    def set_variable(self, value, key):
        self.varibales[key] = value


duck = Animal(color = "red", feet = 5)
print(duck.get_variable("feet"))

STEP 2:
'''
class Animal():
    
    def __init__(self,**kwargs):
        self._color = kwargs.get("color", "white")
    
    def quack(self):
        print("Quacking ....!!!!!!!!!")

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value


duck = Animal(color = "red")
print(duck.get_color())
duck = Animal(weight = 50)
print(duck.get_color())

"""
STEP1 : 

class Animal():
   
    # _variable - is used to mention explicitly that the variable is intended 
    #to use only within the class 
    def __init__(self,color = "white"):
        self._color = color
    
    def quack(self):
        print("Quacking ....!!!!!!!!!")

    #Inorder to the access the variable _color, the object has to access it 
    #through this function
    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value


duck = Animal()
print(duck.get_color())
duck.set_color("Blue")
print(duck.get_color())
"""
