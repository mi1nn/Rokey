# function_call.py

# 절대값 출력
# print(myabs(10)) 호이스팅 불가능

def myabs(arg):
    if (arg < 0):
        result = arg * -1
    else:
        result = arg
    return result

print(myabs(10))
print(myabs(-10))

print('---------------------------')

def funca():
    print("a 함수 호출")

def funcb():
    funca()
    print("b 함수 호출")
    
def funcc():
    funcb()
    print("c 함수 호출")
    
funcc()

print('---------------------------')

# 문제1
def draw_stars(num):
    print('*' * num)

draw_stars(3)
draw_stars(2)
draw_stars(1)

print('---------------------------')

# # 문제2
# def fmul(a, b):
#     return a * b
# def fsub(a, b):
#     return a-b
# def fadd(a, b):
#     return a + b
# def fdiv(a, b):
#     return a / b

# na = int(input("첫번째 숫자 입력: "))
# nb = int(input("두번째 숫자 입력: "))

# nc = fadd(na, nb)
# print(na, " + ", nb, " = ", nc)
# nd = fsub(na, nb)
# print(na, " - ", nb, " = ", nd)
# ne = fmul(na, nb)
# print(na, " * ", nb, " = ", ne)
# nf = fdiv(na, nb)
# print(na, " / ", nb, " = ", nf)

print('---------------------------')

# 문제3  len 함수 구현
sta = "python example"

def string_length(stb):
    count = 0 
    for letter in stb:
        count += 1
    return count
  
lena = string_length(sta)
print(lena)

print('---------------------------')

# 문제4

na = float(input("첫번째 숫자: "))
nb = float(input("두번째 숫자: "))

def diva(a, b):
    if b == 0:
        print("나눌 수 없다")
    else:
        return a / b

print(diva(na, nb))