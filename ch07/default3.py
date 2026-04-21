# default3.py

def personA(width = 11, height = 21):
    print("함수 기본값 없음")
    print("width: ", width, end=" ")
    print("height: ", height)
    print()

def personB(width = 4, height = 3):
    print("함수 기본값 있음")
    print("width: ", width, end=" ")
    print("height: ", height)
    print()
    
personA(10, 20)   # 인수 우선 순위 더 높음
personA()
personB()


# 1. 모든 매개변수에 기본값 설정 가능
# 2. 인수 전달 시 앞에서부터 설정 가능
# 3. 기본값에 있더라도 인수를 설정 가능 (인수 우선 처리)
# 4. 부분 매개변수에 기본값 설정 시 뒤에서부터 설정할 것


# 위치 인수: 순서대로 전달하는 인수
personA(10)
# 키워드 인수: 이름을 지정해서 전달하는 인수
personA(height = 30)

print()
print('--------------------')
print()

# person_lee 사람 함수 생성
# 기능/동작: 3가지 데이터를 확인(출력)
# 함수 내 전달되는 데이터(매개변수): 몸무게, 키, 나이
# 반환값: 없음

def person_lee(weight = 79, height = 178, age = 29):
    print("몸무게: ", weight, end = " ")
    print("키: ", height, end = " ")
    print("나이: ", age)
    print()

person_lee(81, 181, 30)
# 1. 모든 매개변수에 기본값 설정 가능
person_lee()

# 2. 인수 전달 시 앞에서부터 설정 가능
person_lee(55)
person_lee(55, 168)

# 3. 기본값에 있더라도 인수를 설정 가능 (인수 우선 처리)
def person_lee2(weight, height, age = 29):
    print("몸무게: ", weight, end = " ")
    print("키: ", height, end = " ")
    print("나이: ", age)
    print()
    
person_lee2(40, 177)
person_lee2(40, 177, 39)

# 4. 부분 매개변수에 기본값 설정 시 뒤에서부터 설정할 것
def person_lee3(weight, height, age = 29):
    print("몸무게: ", weight, end = " ")
    print("키: ", height, end = " ")
    print("나이: ", age)
    print()
    
person_lee3(weight = 68, height = 40)
