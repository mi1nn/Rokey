# search.py

import re
p = re.compile("[a-z]+")
# m = p.search("python")   # python
# m = p.search("3 python")   # None
m = p.search("3 py8thon")   # py
# print(m)

if m: 
    print("Matched: ", m.group())
else:
    print("Not matched")
    
print('----------------------')
p = re.compile("Python")
m = p.search("The mission of the Python software...")
print(m)