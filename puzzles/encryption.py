'''
solution to the below puzzle:
https://www.hackerrank.com/challenges/encryption/problem
'''

from math import ceil, sqrt
from string import whitespace

def encrypt(string):
    enc_string = string.translate(None,whitespace)
    length = len(enc_string)

    #calculate the no of colums for the grid
    columns = int(ceil(sqrt(length)))

    #form a list of strings each of length equal to columns
    split_string = [enc_string[i:i+columns] for i in range(0, len(enc_string), columns)]

    #encrypted list of strings
    new_string = ['']*columns
    for string in split_string:
        for i, char in enumerate(string):
            #replace the element in the list with the new string
            new_string[i] += char

    return " ".join(new_string)

if __name__ == "__main__":
    s = raw_input().strip()
    result = encrypt(s)
    print(result)
