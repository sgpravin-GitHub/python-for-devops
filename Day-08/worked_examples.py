#**Q2: How do you create a list in Python, and can you provide an example related to DevOps?**

color_list=["orange","red","yellow","blue"]

#What is the difference between a list and a tuple in Python

color_list=["orange","red","yellow","blue"]
color_tuple = ("while", "black")

#note- differences
# once tuple is defined, we can't modified but in list we can add or remove items in that
# in list , we can append, delete but in tuple we cant'
# reading of list will be slow but tuple is very fast as it will store CONTINUOUSLY in the memory when its defined it

#--------
#How can you access elements in a list, and provide a DevOps-related example?**
color_list=["orange","red","yellow","blue"]
print(color_list[0])
print(color_list[1])

#---------------
# How do you add an element to the end of a list in Python? Provide a DevOps example.**
color_list=["orange","red","yellow","blue","yellow"]
color_list.append('black')
color_list.append('white')

print(color_list)
#---------------
# How can you remove an element from a list in Python, and can you provide a DevOps use case?**
color_list.remove("black")
color_list.remove("orange")

print(color_list)
color_list.reverse()
print(color_list)

xx = color_list.count("yellow") #The count() method returns the number of times the specified element appears in the list.
print(xx)