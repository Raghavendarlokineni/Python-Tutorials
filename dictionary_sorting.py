from operator import itemgetter, add, sub, truediv, concat, countOf

""" method to sort out dictionary """

list1 = [{'name': 'NAME1', 'age': '18'}, {'name': 'NAME2', 'age': '1'}, \
        {'name': 'NAME3', 'age': '28'}]

print("list is ", list1)

newlist = sorted(list1, key = itemgetter('age'))
print("newlist is ", newlist)



""" few other examples which demonstrates operator module 
a = 10
b = 5

print("a+b is " , add(a,b))
print("a-b is " , sub(a,b))
print("a-b is " , truediv(a,b))

c = "Hello"
d = "operator"
print("concat c,d is " , concat(c,d))

e = "Hello operator"
f = 'o'
print(" count of 'o' in {} is {}" .format(e, countOf(e,f)))  

"""
