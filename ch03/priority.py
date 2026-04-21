# priority.py

# 연산자 우선순위
num1 = 2 * (3 - 5)
print(num1)

num2 = 1 > (2 and 3) + 3
print(num2) # False

print(2 and 3) # 3
print(0 and 3) # 0
# 앞 값이 True -> 뒤의 값 반환
# 앞의 갓이 False -> 앞의 값 반환

print(9 > 4 and 3 > 2)
print(True and True)

print(9 < 4 and 3 > 2)
# False and True
print(9 < 4 or 3 < 2)
# False or False
print(9 < 4 or 3 > 2)
# False or True

print('----------------')
# 문제 1
print(9 < 4 or 3 < 2 and 4 > 2)
# False or False and True  -> False

# 문제 2
print((3 - 5) + 3 < 1 and 3 - 5 > 1)
# False and False  -> False

# 연산자 우선순위
# 괄호 > 산술 > 비교 > 논리 > 대입

# 논리 연산자 우선순위
# not > and > or

# 산술 연산자 내 우선순위
# ** * / // %: 제곱 곱셈 나눗셈 몫 나머지
# +x, -x: 단항연산자