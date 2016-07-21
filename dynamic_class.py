"""
this module demonstrates the addition of a function in a class dynamically
"""

from types import MethodType

class myclass(object):

    def __init__(self, val):
        self.val = val
        
"""
method 1, function can only be used by object with which it is bounded to. 

self is required in the function to bind it with object """

def add(self, value):
    print("method 1 : add result is",self.val + value)


a = myclass(20)

a.add = MethodType(add, a)
a.add(10)

""" method 2 , funcation can be used by different objects """

def sub(self, num):
    print("method 2: sub result is",self.val - num)

myclass.sub = sub

b = myclass(20)
b.sub(10)

c = myclass(30)
c.sub(10)
