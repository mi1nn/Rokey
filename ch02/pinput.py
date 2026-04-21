# pinput.py

print("첫 번째 정수를 입력하세요: ")
ra = input()
print(type(ra))

rb = input("두 번째 정수를 입력하세요: ")
print(type(rb))

# "5"


# 1. 문자열 연결 연산자 -> str() + str()
# 2. 산술 연산자 -> int() + int()

rc = ra + rb
# rc = int(ra) + int(rb)

print(ra, "+", rb, "=", rc)