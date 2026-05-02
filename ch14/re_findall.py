# re_findall.py

import re
p = re.compile("[a-z]+")
m = p.findall("life is too short")   
print(m)  # ['life', 'is', 'too', 'short']
m = p.findall("3 py8thon")  
print(m)  # ['py', 'thon']
    
print('----------------------')
p = re.compile("Python")
m = p.findall("The mission of the Python software...")
print(m)  # ['Python']