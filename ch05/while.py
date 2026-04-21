# while1.py

# (조건식에 사용된) 변수 초기화
# while 조건(식):
#     코드블럭
#     while문을 빠져나올 수 있는 조건식

# while True:
#     print('ctrl + c 입력')

a = 10
b = 5

a = a - b
print(a)

print()

a = 10
b = 5

a -= b
print(a)

print('-------------------')

num = 0
while num < 3:
    print('안녕 거북아', num)
    # num = num + 1
    num += 1

"""
    *= 곱하기 후 대입  ->  a */ = 3 
    /= 나누기 후 대입  ->  a /= 3
    //= 몫 나누기  ->  a //= 3
    %= 나머지  ->  a %=3
    **= 거듭제곱  ->  a **= 3
"""

stra = '파이썬'
strb = '프로그래밍'
stra += strb
print(stra)