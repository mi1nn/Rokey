# re_option.py
# 컴파일 옵션

import re
# 패턴 객체 = re.compile("정규식", 옵션)

# DOTALL, S
# p = re.compile("a.b", re.DOTALL)
p = re.compile("a.b", re.S)
print(p.match("a\nb"))   # "a\nb"

print('-------------------------')

# IGNORECASE, I
# p = re.compile("[a-z]+", re.IGNORECASE)
p = re.compile("[a-z]+", re.I)
print(p.match("python"))   
print(p.match("Python"))   
print(p.match("PYTHON"))   

print('-------------------------')

# MULTILINE, M
# p = re.compile("^python\s\w+", re.MULTILINE)
# p = re.compile("^python\s\w+")  # ['python one']
p = re.compile("^python\s\w+", re.M)   # ['python one', 'python two', 'python three']

data = """python one
life is too short
python two
you need python 
python three
"""

print(p.findall(data))

print('-------------------------')

# VERBOSE, X
# p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);', re.VERBOSE)
# p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);', re.X)

p = re.compile(r"""
               &[#]
               (
                   0[0-7]+
                   |[0-9]+
                   |x[0-9a-fA-F]+
                   )
                   ;
                   """, re.X)
data = "&#07; &#8; &#x0A;"
print(p.findall(data))