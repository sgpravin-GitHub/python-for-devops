import os

input_folder_name = input("enter the folder names with spaces : ")
folder_name = input_folder_name.split()

for folder in folder_name:
    try:
        file = os.listdir(folder)
    except FileNotFoundError:
        print("the folder name entered by you is not proper -> '" + folder + "'")
        continue

    print("=== the files in the folder '" + folder + "' is :")
    print(file)

