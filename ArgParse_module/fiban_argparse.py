"""
module demonstrates the usahe of argparse module by considering the 
fibonacci series
"""

import argparse

def fibonacci(num):
    result = 0
    a, i = 0, 1
    for j in range(num):
        yield a
        a, i = i, a+i

def Main():
 
    parser = argparse.ArgumentParser(description = "fibonacci series calculation")
    
    #type will define the arugument to be a specified type, else it will 
    #throw error
    parser.add_argument("--number", help= "input number", type = int)
    
    #writing out the output to a text file is done by mentioning either -o 
    #or --output
    parser.add_argument("-o", "--output", help =" output to the file" , \
                        action = "store_true") 
    args = parser.parse_args()

     
    if args.output:
    
        #creating a generator object
        for i in fibonacci(args.number):
    
            f = open("fib.txt", "a")
            f.write(str(i) + "\n")
    f.close()
if __name__ == "__main__": Main()
