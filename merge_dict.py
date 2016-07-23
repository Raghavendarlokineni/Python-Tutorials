list1 = {'age': '18', 'name': 'NAME1'}
list2 = {'age': '28', 'place': 'COUNTRY'}

""" method supported in python 3.5 """
list3 = {**list1, **list2}
print(list3)


""" different method in python 2.x """
list4 = list1.copy()
list4.update(list2)

print(list4)

""" multiple dictionary merging """

list5 = {'area' : 'STATE', 'code' : '10000'}
dict1 = [list1, list2, list5]

final_list = {}
for dic in dict1:
    final_list.update(dic)

print("final list is", final_list)
