# local2.py


# 함수 내 a를 전역변수로 선언
b = 0 
print("b의 값: ", b)
b = 1
print("b의 값: ", b)

def scope_test1():
    global a
    a = a + 3
    print("함수 내 a 값: ", a)

a = 0 
print("scope_test() 함수 밖의 a 값: ", a)
scope_test1()
print("scope_test() 함수 호출 후 a 값: ", a)

print()
print('---------------------------')
print()


# 함수 내 a를 지역변수로 초기화
b = 0 
print("b의 값: ", b)
b = 1
print("b의 값: ", b)

def scope_test2():
    a = 0
    a = a + 3
    print("함수 내 a 값: ", a)

a = 0 
print("scope_test() 함수 밖의 a 값: ", a)
scope_test2()
print("scope_test() 함수 호출 후 a 값: ", a)

