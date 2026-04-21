# local1.py

b = 0   # 전역변수 선언(초기화)
print("b의 값: ", b)
b = 1   #
print("b의 값: ", b)

def scope_test():
    global a  # 전역 변수로 
              # 변수 생성 선언은 아님
    a = 1   # 지역변수가 아닌 전역변수
    print("scope_test() 함수 안의 a 값: ", a)

a = 0 
print("scope_test() 함수 밖의 a 값: ", a)
scope_test()
print("scope_test() 함수 호출 후 a 값: ", a)

# 실무 관점 -> global 가능하면 안 쓰는 게 좋음
# 이유: 디버깅 어려움, 사이드 이펙트, 함수의 재사용성이 떨어짐
# 사이드 이펙트: 함수의 결과 외에 외부 상태를 변경하는 것

count = 0
def increment():
    global count 
    count += 1
    
# def increment(count):
#     return count + 1
    
increment()
increment()
print(count) # 2
print()

print('------------------')

count = 100
increment()
print(count)

print('------------------')

def process():
    increment()  # 내부에서 count 값을 변경
# process() 함수만 봐서는 count가 바뀌는 것을 알 수 없다. 
    