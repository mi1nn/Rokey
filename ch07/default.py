# default.py

# def 함수명(매개변수1, 매개변수2, ...):
#     코드블럭
#     return 반환값

# 함수명(인수, 인수2, ...)

def personA(width, height):
    print("함수 기본값 없음")
    print("width: ", width, end=" ")
    print("height: ", height)
    print()

# def personA():   # 오버로딩
#     print("매개변수 없는 함수")
#     print()

def personB(width = 4, height = 3):
    print("함수 기본값 있음")
    print("width: ", width, end=" ")
    print("height: ", height)
    print()
    
# 함수가 재정의되면 기존 함수보다 재정의 함수의 우선순위가 높음

personA(10, 20)   # 인수가 없어야 동작

# personA()  # 인수가 없어서 에러 발생

personA(30, 40)
personB()  # 인수 없어도 정상 실행 -> 함수에 인수를 기입해둠
personB(50, 60)  # 기본값보다 인수에 대한 우선순위가 높음

