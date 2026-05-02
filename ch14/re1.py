# re1.py

# 정규표현식 (Regular Expression)
# 문자열 패턴 정의해서
# 검색, 검사, 치환, 추출 등 수행하는
# 문자열 처리 규칙

import re
# 패턴객체: "검색대상문자열"에서 패턴의 발견을 도와주는 객체
# 정규표현식을 정의해서 compile() 함수의 인수로 전달하면 패턴 객체 반환함

# 메터 문자: 별도의 의미가 담긴 문자

# [] 문자
# - [] 사이에는 대부분 문자(기호) 포함 가능
# - 메타문자도 사용 가능 (대부분 별도 의미 없음)
# - 단, 일부 메타 문자는 의미가 있음

# [abc]: a, b, c 중 한개의 문자와 매치

# 정규표현식 문법
# 패턴 객체: re.compile("정규표현식") # 패턴(규칙) 생성
# 매치객체명 = 패턴객체명.match("검색대상문자열")
# print(매치객체명)

# match() 함수: 문자열 처음부터 정규(표현)식과 매치되는지 조사

p = re.compile("[abc]")
# m = p.match("a") # a
# m = p.match("before") # b
m = p.match("dude") # None
print(m)

print('---------------------')
p = re.compile("[ab]")
print(p.match("apple"))  # match = 'a'
print(p.match("banana")) # match = 'b'  
print(p.match("dude"))   # None

print('---------------------')
p = re.compile("ab")
print(p.match("apple"))  # None
print(p.match("banana")) # None
print(p.match("dude"))   # None
print(p.match("absolute"))   # match = 'ab'
print(p.match("kabsolute"))   # None

print('---------------------')
p = re.compile("[0-5]")
print(p.match("1apple"))  # match = '1'
print(p.match("2banana")) # match = '2'  
print(p.match("7dude"))   # Non

print('.(doot), +(plus)------------------')
p = re.compile("[.abc]")
print(p.match(".apple"))  # match = .
p = re.compile("[+abc]")
print(p.match("+banana"))   # match = '+'

print('^(carrot)-----------------')
p = re.compile("[^abc]")  #부정 (not) 의미
print(p.match("^apple"))  # match = '^'
print(p.match("apple")) # None
print(p.match("banana"))   # None
print(p.match("melon"))   # match = 'm'

print('---------------------')
p = re.compile("[\^abc]")   # ^을 not의 의미가 아닌 문자 그대로 사용
print(p.match("^apple"))  # match = '^'
print(p.match("banana")) # match = 'b'  
print(p.match("dude"))   # None

print('---------------------')
p = re.compile("[a-zA-Z]")   # 모든 알파벳
print(p.match("apple"))  # match = 'a'
print(p.match("Banana")) # match = 'B'  
print(p.match("dude"))   # match = 'd'

print('---------------------')
p = re.compile("\D")  # [0-9]
print(p.match("1apple"))  # None
print(p.match("Banana")) # match = 'B'
print(p.match("7dude"))   # None

print('---------------------')
p = re.compile("\s")   # [\t\n\r\f\v]
p = re.compile("\S")   # [^ \t\n\r\f\v]
print(p.match("apple"))  # None
print(p.match("\tbanana")) # None
print(p.match("\ndude"))   # None

print('---------------------')
p = re.compile("\w")  # [a-zA-z0-9_]
p = re.compile("\W")  # [^ a-zA-z0-9_]
print(p.match("1apple"))  # match = '1'
print(p.match("Banana")) # match = '2'  
print(p.match("3melon"))   # None
print(p.match("_orange"))   # None

print('---------------------')
# . 문자
p = re.compile("a.b")
print(p.match("aab"))   # aab
print(p.match("a0b"))   # a0b
print(p.match("abc"))   # None
print(p.match("a\tb"))  # a\tb
print(p.match("a\nb"))  # None

p = re.compile("a[.]b")
print(p.match("aab"))   # None
print(p.match("a.b"))   # a.b

print('---------------------')
# * 문자
p = re.compile("a*")
print(p.match("apple"))  # a
print(p.match("aaaapple"))   # aaa

p = re.compile("ca*t")
print(p.match("ct"))  # ct
print(p.match("cat"))   # cat
print(p.match("caaaat"))   # caaaat
print(p.match("cbt"))   # None

print('---------------------')
# + 문자
p = re.compile("ca+t")
print(p.match("ct"))  # None
print(p.match("cat"))   # cat
print(p.match("caaaat"))   # caaaat
print(p.match("cbt"))   # None
print(p.match("c t"))   # None

print('---------------------')
# {} 문자: {m} {m, n} {m,} {,n}
p = re.compile("ca{2}t")
print(p.match("ct"))  # None
print(p.match("cat"))   # None
print(p.match("caaaat"))   # None
print(p.match("cbt"))   # None
print(p.match("caat"))   # caat

print('---------------------')
# ^ 문자
p = re.compile("^hello")
print(p.match("hello world! "))  # hello
print(p.match(" hello world "))  # None
print(p.match("\nhello world"))  # None
print(p.match("pello world"))  # None

print('---------------------')
# $ 문자
p = re.compile("world$")
print(p.search("hello world! "))  # None
print(p.search(" hello world "))  # None
print(p.search("hello world\n"))  # world
print(p.search("pello world"))  # world
# match: 문자열의 시작부분부터 패턴과 일치하는 지 확인
# 즉, $를 사용해도 문자열 끝을 찾을 수 없음
# search: 문자열의 전체를 검색하여 패턴 일치하는 지 확인
# $는 search()와 함께 사용하는 것이 일반적

