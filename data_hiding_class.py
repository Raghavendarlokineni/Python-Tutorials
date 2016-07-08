class hiding():
    __hideAttr = 10

    def func(self):
        self.__hideAttr += 1 
	print(self.__hideAttr)

a = hiding()
a.func()
a.func()

#accessing a hidden attribute results in error, comment out below line for removing the error
#AttributeError: 'hiding' object has no attribute '__hideAttr'
print (a.__hideAttr)

#to access hidden attributes of a class
print (a._hiding__hideAttr)
