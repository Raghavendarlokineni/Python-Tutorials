"""
module demonstrates the usage of some of the action items in argparser
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--a", action = "store_const", const = 42)
parser.add_argument("--b", action = "store_true")
parser.add_argument("--c", action = "store_false")
parser.add_argument("--d", action = "store_false")

args = parser.parse_args()

print(args.a)
print(args.b)
print(args.c)
print(args.d)

"""
root@labadmin-VirtualBox:~/RAGHU/python# python test2.py --help
usage: test2.py [-h] [--a] [--b] [--c] [--d]

optional arguments:
  -h, --help  show this help message and exit
  --a
  --b
  --c
  --d
#as the optional arugument is provided for a, the value 42 is stored to the 
#varibale and if the arugument -a is not provided it takes the default value 
#42 that we have provided, and for store_true, the variable will be True when the 
#arugument is provided and for store_flase, the varibale will be False when 
#the argument is provided. The same can be observed in the following outputs.

root@labadmin-VirtualBox:~/RAGHU/python# python test2.py --a
42
False
True
True


root@labadmin-VirtualBox:~/RAGHU/python# python test2.py --b
None
True
True
True

root@labadmin-VirtualBox:~/RAGHU/python# python test2.py --c
None
False
False
True

root@labadmin-VirtualBox:~/RAGHU/python# python test2.py --d
None
False
True
False

"""
