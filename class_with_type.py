""" module demonstrates the creation of class using 'type'

    CLASS_NAME = type('OBJECT_NAME', (INHERITED_CLASS), {PARAMTERS})

    type returns a class in CLASS_NAME with object name as 'OBJECT_NAME' which
    inherits the properties of 'INHERITED_CLASS'. This could be empty if class
    doesn't need of inherited class.

    PARAMTERS is a dictionary which will be converted as the paramters of the
    class.
"""

myclass = type('class1', (), {'a' : '1'})

""" output of the below command is :
<class '__main__.myclass'>
It is clear now that class can be created with 'type'
"""
print(myclass)

"""accessing a variable of the class """
print(myclass.a)

""" child class with inheritance """
child = type('class2', (myclass,), {'b' :'2', 'c' : '3'})

print(child)
print('a in myclass is ', myclass.a, 'a in child is', child.a)
print('b is ', child.b, 'c is ', child.c)


""" dynamic addition of functions/methods were covered in different module
in dynamic_class.py """
