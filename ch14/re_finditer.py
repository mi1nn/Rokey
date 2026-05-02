# re_finditer.py

import re
p = re.compile("[a-z]+")
result = p.finditer("life is too short")   
print(result)  # iterator object

for i in result:
    print(i)  # match object

print('----------------------')
p = re.compile("Python")
results = p.finditer("The mission of the Python software...")
print(results)  # ['Python']

# print(list(results))
for m in results:
    print("매치 문자열: ",m.group())  
    print("문자열 위치: ", m.span())
    print("문자열 시작위치: ", m.start())
    print("문자열 끝위치: ", m.end())