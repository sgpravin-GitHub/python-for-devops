def update_conf_file(file_path, key, value):

    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if(key in line):
                file.write(key + " = " + value + "\n")        #TIMEOUT = 300
            else:
                file.write(line)


update_conf_file("D:\Python_4_devops\python-for-devops-main\Day-12\server.conf", "PORT", "8080")

#update_conf_file("D:\Python_4_devops\python-for-devops-main\Day-12\temp.conf", "MAX_CONNECTIONS", "200") #this is not working
print(".......done......")