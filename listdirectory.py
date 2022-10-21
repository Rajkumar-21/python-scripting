import os
path = input("Enter the path to list your directories: ")
result = print(os.listdir(path))

fileout = os.path.isfile(path)
print(fileout)