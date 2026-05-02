# lambda1.py

# lambda 매개변수: 표현식

# 일반적인 함수 정의 및 호출
# def 함수명(매개변수):
#     코드블럭
#     return 반환값
# 함수명(인수)

def add(x):
    return x + x
print(add(2))

print('-----------------')
# 람다 함수의 정의 및 호충
# 사용 목적: 이름이 필요없는 짧은 함수를 한번 사용
add2 = lambda x: x + x
print(add2(5))

print('-----------------')
print((lambda x: x+x) (2))

print('-----------------')
square = lambda x: x ** 2
print(square(3))
print((lambda x: x ** 3) (6))

# 조건문: 다능 (단, 표현식 형태만)
# 반복문 -> 불가능