# re_match.py

import re
p = re.compile("[a-z]+")
m = p.match("python")   # python
# m = p.match("3 python")   # None
print(m)

if m: 
    print("Matched: ", m.group())
else:
    print("Not matched")