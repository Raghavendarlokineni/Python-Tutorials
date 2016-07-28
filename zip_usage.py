"""
This module demonstrates the funtionality of 'zip()'
zip(list1, list2...., listn) combines all the lists and returns a list of tuples.

EXAMPLE - 1
"""

day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
num = [1, 2, 3, 4, 5, 6, 7]

week = zip(num, day)

for a in week:
    print(a)

"""
output :
(1, 'monday')
(2, 'tuesday')
(3, 'wednesday')
(4, 'thursday')
(5, 'friday')
(6, 'saturday')
(7, 'sunday')

"""

"""
EXAMPLE - 2
"""

sub = ['maths', 'science', 'social']

marks = [35, 70, 100]

result = []

for mark in marks:
    if mark <= 40:
        result.append("fail")
    elif 40 < mark <= 70:
        result.append("grade2")
    elif 70 < mark <= 100:
        result.append("grade1")

report = zip(sub, marks, result)

for s, m, r in report:
    print("subject : ", s, "|| marks : ", m, "|| result : ", r)
    
"""
output :

subject :  maths || marks :  35 || result :  fail
subject :  science || marks :  67 || result :  grade2
subject :  social || marks :  89 || result :  grade1

"""
































