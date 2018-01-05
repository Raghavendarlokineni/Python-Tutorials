'''
solution to the below puzzle:
https://www.hackerrank.com/challenges/encryption/problem
'''

from math import ceil, floor, sqrt
from string import whitespace

def encrypt(string):
    enc_string = string.translate(None,whitespace)
    length = len(enc_string)
    rows = int(floor(sqrt(length)))
    columns = int(ceil(sqrt(length)))
    split_string = [enc_string[i:i+columns] for i in range(0, len(enc_string), columns)]
    new_string = []
    for string in split_string:

        for i in range(len(string)):
            try:
                new_string[i] = new_string[i].replace(new_string[i], new_string[i] + string[i])
            except IndexError:
                new_string.append(string[i])

    return " ".join(new_string)

if __name__ == "__main__":
    s = raw_input().strip()
    #s = "if man was meant to stay on the ground god would have given us roots"
    result = encrypt(s)
    print(result)
