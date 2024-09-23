#This function will ask the use the give the folder name and then 
# it will list the files present in that folder

import os
folder_name = input("please enter the folder names with spaces for which you need to see the files present in that folder: ").split()

for folder in folder_name:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("The folder name which you entered doesnot exists: " + folder)
        continue

    print("=== files in the " + folder)
    files = os.listdir(folder)
    print(type(files))
    print(files)