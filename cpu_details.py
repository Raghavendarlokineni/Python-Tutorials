import os
import sys

os.system("lscpu > cpu.log")

dict = {}
with open("cpu.log", "r+") as f:
    for line in f:
        word = line.split(":")
        
        #using the strip to remove unwanted spaces while stroing the values in dictionary
        dict[word[0]] = word[1].strip()

if ((len(sys.argv) <= 1) or (len(sys.argv) > 2)):
    print "usage is cpu.py 'paramter'"
    for count in dict:
        print "--"+count+"--"
else:
    for count in dict:
        if(sys.argv[1] == count):
            print("value of %s is %s" % (count, dict[count]))
