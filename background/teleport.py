'''import os





def teleport(path, to):


    file = open(path, "rb")
    to = open(to, "wb")

    to.write(file.read())
    file.close()
    to.close()
print(os.listdir())'''
import os
print(os.getcwd())