# function1.py

# # 함수 정의
# def 함수명(매개변수):
#     코드블럭
#     return 반환값

# def 함수명():
#     코드블럭

# 함수명(인수1, 인수2, ...)

# 기능/동작: 토끼에게 인사
# 입력(매개변수): 없음
# 출력(반환값): 없음

def my_func():
    print('토끼야 안녕!')
    print('사자야 안녕!')
    print('거북아 안녕!')
    print('코끼리야 안녕!')

# 호출(사용)
my_func()

print()

# 매개변수 = 인수

def fhello():
    print("매개변수 없는 함수 호출")

fhello()
print()

print('------------------------------')

def funca(na, nb):
    nc = na + nb
    print(na, " + ", nb, " = ", nc)

funca(10, 20)
print()

print('------------------------------')

# add 함수 구현

def add(num1, num2):
    return num1 + num2

print(add(2, 3))

# minus 구현

def minus(num1, num2):
    return num1 - num2

print(minus(5, 3))

