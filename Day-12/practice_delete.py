#this file shows the file operations

def update_conf_file(file_path, key, value):

    with open(file_path,"r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if(key in line):
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


update_conf_file("server.conf", "TIMEOUT", "999")