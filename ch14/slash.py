# slash.py

import re
# p = re.compile("\section")  # None
# p = re.compile("\\section")  # None
p = re.compile("\\\\section")   # \\section
print(p.match("\section python hello thanks"))

# '\\section'으로 보이는 이유?
# 문자열 안의 백슬래시를 구분하기 위해 escape해서 보여주기 때문

# 1. 파이썬 리터럴 규칙 (이스케이프)
# "\\" -> "\"
# "\\\\" -> "\\"
# 2. '\s' 정규표현식 화이트스페이스 의미
# "\\section" -> "\section"

## raw string
# -> 파이썬 문자열 리터럴 안에서 \n, \t 같은 "이스케이프 코드 처리"를 없애주는 역할

print('-------------------')
p = re.compile("\new")   # \new
print(p.match("\new python hello thanks"))
