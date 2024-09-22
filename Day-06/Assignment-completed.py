## Task 1: Arithmetic Operators
#1. Create two variables `a` and `b` with numeric values.
#2. Calculate the sum, difference, product, and quotient of `a` and `b`.
#3. Print the results.
#----------
a=10
b=20

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def multi(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

print("Question-1 Answers:")
print("addition of two numbers : " , add(a,b))
print("subtraction of two numbers : " , sub(a,b))
print("multiplication of two numbers : " , multi(a,b))
print("division of two numbers : " , div(a,b))

#********************************
## Task 2: Comparison Operators
#1. Compare the values of `a` and `b` using the following comparison operators: 
# `<`, `>`, `<=`, `>=`, `==`, and `!=`.
#2. Print the results of each comparison.
#-----
x=100
y=200

print("Question-2 Answers:")
if (x>y):
    print(x , " is greater than " , y)
else:
    print(x , " is smaller than " , y)
#*************************
## Task 4: Assignment Operators
#1. Create a variable `total` and initialize it to 10.
#2. Use assignment operators (`+=`, `-=`, `*=`, `/=`) to update the value of `total`.
#3. Print the final value of `total`.
print("Question-4 Answers:")
total=10
total += total
print("value of total after using += is ", total)

total=10
total -= total
print("value of total after using -= is ", total)

total=10
total *= total
print("value of total after using *= is ", total)

total=10
total /= total
print("value of total after using /= is ", total)

#************************************
## Task 6: Identity and Membership Operators
#1. Create a list `my_list` containing a few elements.
#2. Use identity operators (`is` and `is not`) to check if two variables are the same object.
#3. Use membership operators (`in` and `not in`) to check if an element is present in `my_list`.
#4. Print the results.

#colors = ["red","blue","yellow","orange","brown"]
#new_color= ["red","blue","yellow","orange","brown"]

colors = 10
new_color= 10

print("Question-6 Answers:")
if (new_color is not colors):
    print("both are same")
else:
    print("both are NOT same")

print(id(colors))
print(id(new_color))

#Note- if both variables id is same then only it will print as same else it won't print as same
#in case of list, the id's of both the variables are not same
#in case of assigning 10 for both the variables, id's will be same