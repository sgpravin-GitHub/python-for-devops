import sys
import os

def add(num1, num2):
    total=num1+num2
    return(total)

def sub(num1, num2):
    total=num1-num2
    return(total)

def multi(num1, num2):
    total=num1*num2
    return(total)

def div(num1,num2):
    total=(num1/num2)
    return(total)

# this to read the command line arguments(example: python calculator.py 5 add 25)
#-------------
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])
#-------------

if (operation == "add"):
    print(add(num1,num2))
elif (operation == "sub"):
    print(sub(num1, num2))
elif (operation == "multi"):
    print(multi(num1, num2))
else:
    print(div(num1,num2))

#before running this file, define the environment variables
#export fname="pravin"
#export lname="kumar"
#export password="test@123"
#export tokenpin="adfadsferq3324kj"

print("first name is :", os.getenv("fname"))
print("last name is : ", os.getenv("lname"))
print("password is : ", os.getenv("password"))


