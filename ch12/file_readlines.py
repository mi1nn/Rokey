# file_readlines.py

path = r"ch12/file1.txt"
f = open(path, "r")

lines = f.readlines()
print(type(lines))

for line in lines:
    print(line, end = " ")
    
f.close()
