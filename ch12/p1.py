# p1.py

import os 
print(os.getcwd())

path = r"ch12/account1.txt"
mode = "w+"
encodings = "utf-8"
f = open(path, mode)

# f.write("김삿갓 597-89-000089 \n")
# f.write("이수근 343-64-000064 \n")
# f.write("박혁거세 136-97-000097 \n")

# f.seek(0)
# print(f.read())

# f.close()

with open(path, mode, encoding = encodings) as file:
    f.write("김삿갓 597-89-000089 \n")
    f.write("이수근 343-64-000064 \n")
    f.write("박혁거세 136-97-000097 \n")

