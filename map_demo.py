"""
map(function, sequence) is a in-built function which takes 2 arguments, function and a list.
It returns the list of values which are results of that function 
"""
"""
USER DEFINED MAP FUNCTION
"""

def square(x):
    return x*x

def my_map(func, seq):
    List = []
    for val in seq: List.append(func(val))
    return List

print(my_map(square, [1,2,3,4]))

"""
EXAMPLE: 
List of functions can also be passed as an arugument for map

def square(x):
    return x*x

def add(x):
    return x+x

List = [square, add]

a = [1,2,3,4]

for i in a:
    result = map(lambda fun:fun(i) ,List)

    print(result) 
"""

"""
EXAMPLE:
A function can be passed with lambda as well. 

a = [1,2,3,4]

b = map((lambda x: x*x), a)
print(b)

"""
"""
EXAMPLE 

a = [1,2,3,4]
def square(x):
    return x*x

b = map(square, a)
print(b)
"""
