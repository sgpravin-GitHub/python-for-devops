#This function will show how to use try & except block using ZeroDivisionError

import sys

print("please provide 2 numbers to find the division of them")

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

try:
    result = num1 / num2
except ZeroDivisionError:
    print("please provide the value greater than ZERO")
    exit()

print(result)
