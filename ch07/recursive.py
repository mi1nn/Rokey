# recursive.py 

# 재귀함수
# def 함수명(매개1, 매개2, ...):
#     코드블럭
#     함수명(인수1, 인수2, ...)
#     return 반환값

def countdown(n):
    if n == 0:
        print("완료!")
        return 
    print(n)
    countdown(n - 1)

countdown(5)

# 반복문과 재귀함수의 효율성 비교
# for 반복문이 좋은 경우: 함수 호출 내용이 큰 경우, 반복 횟수가 많은 경우 (수만 ~ 수십만 이상)
# 재귀함수가 좋은 경우: 알고리즘 문제 / 트리 구조, 코드 가독성에서 유리
