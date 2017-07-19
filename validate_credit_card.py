import re

pattern = '^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

total_count = int(raw_input())
numbers_list = []

for count in range(total_count):
    numbers_list.append(raw_input())

def check_seq(num):
    for i, n in enumerate(num):
        try:
            if (num[i], 
                num[i+1],
                num[i+2],
                num[i+3]
               ) == (n,n,n,n):
               return False 
        except IndexError:
            pass
    return True
def check_valid(num):
     """Returns `True' if the sequence is a valid credit card number.

     A valid credit card number
     - must contain exactly 16 digits,
     - must start with a 4, 5 or 6 
     - must only consist of digits (0-9) or hyphens '-',
     - may have digits in groups of 4, separated by one hyphen "-". 
     - must NOT use any other separator like ' ' , '_',
     - must NOT have 4 or more consecutive repeated digits.
    """
    match = re.match(pattern, num)
    if match != None and check_seq("".join(num.split("-"))):
       return "Valid"
    else:
       return "Invalid"

if __name__ == "__main__":
    for num in numbers_list: 
        print(check_valid(num))
