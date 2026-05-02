# re_compile.py

import re

# 축약 전 형태
p = re.compile("[a-z]+")
m = p.match("python")   # python
print(m)

# 축약 후 형태
# 매치 객체 = re.match("정규식", "검색대상문자열")
p = re.match("[a-z]+", "python")
p = re.match("[a-z]+", "3 py8thon")
print(m)