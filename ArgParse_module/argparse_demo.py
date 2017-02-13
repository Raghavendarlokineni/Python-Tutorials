"""
positional aruguments are mandatory
--argument will make the arugument optional

When operating with multiple optional arguments the following syntax will
thorw an error as below:
>python argparse_demo.py 1 add
>usage: argparse_demo.py [-h] [--number1 NUMBER1] [--number2 NUMBER2]
                        [--operation OPERATION]
>argparse_demo.py: error: unrecognized arguments: 1 add
The arugumets should be passed when above error is occured:
>python argparse_demo.py --number1 1 --number2 2 --operation add
OUTPUT:
1
2
add
3
"""
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--number1", help = "first number")
    parser.add_argument("--number2", help = "second number")
    
    #User can be restricted with options avilable in our program with choices
    parser.add_argument("--operation", help = "operation", \
                       choices = ["add", "sub", "multiply"])
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.operation)
  
    if args.operation == "add":
        print(int(args.number1) + int(args.number2))
    elif args.operation == "sub":
        print(int(args.number1) - int(args.number2))
    if args.operation == "multiply":
        print(int(args.number1) * int(args.number2))
