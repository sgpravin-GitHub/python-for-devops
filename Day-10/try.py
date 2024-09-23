import os
f_name = input("enter the folder name with spaces : ")
folder_name = f_name.split()

for folder in folder_name:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("the folder name you entered is not proper " + folder)
        continue

    print("+++++++ files present in '" + folder + "' is +++++++")
    files = os.listdir(folder)
    print(files)
