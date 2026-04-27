# file_read.py

path = r"ch12/file1.txt"
f = open(path, "r")

data = f.read()
# data = f.read(5)
print(type(data))
print(data)
    
f.close()
