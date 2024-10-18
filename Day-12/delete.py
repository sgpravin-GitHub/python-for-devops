# this file shows how we can use file operations

def update_conf_file(file_path, key, value):

    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if (key in line):
                file.write(value + " = " + "300" + "\n")      #TIMEOUT = 300
            else:
                file.write(line)
    

update_conf_file("D:\Python_4_devops\python-for-devops-main\Day-12\server.conf", "TIMEOUTssss", "TIMEOUT")
print("done.....")

#to run the python file, we have to run the following commands
# python .\<filename>.py

