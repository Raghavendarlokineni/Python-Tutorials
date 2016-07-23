class calculator():

    def add(self, a, b, c):
        print("addition result is ", a + b + c)

    def avg(self, a, b, c):
        print("avg sum is ", (a+b+c)/3)

    def multiply(self, a, b, c):
        print("multiplication result is ", a*b*c)

List = [1, 2, 3]

calc = calculator()

print("accessing arguments in a regular procedure ")
calc.add(List[0], List[1], List[2])
calc.avg(List[0], List[1], List[2])
calc.multiply(List[0], List[1], List[2])

"""

procedure to unpack the arguments using a list
func(*list) - '*' before the list will unpack the aruguments 

"""

print("\n accessing arguments through unpacking \n")
calc.add(*List)
calc.avg(*List)
calc.multiply(*List)
