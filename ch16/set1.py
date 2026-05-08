# set1.py
# set(세트): 중복을 허용하지 않는 자료구조

# 문법: {데이터1, 데이터2, 데이터3}

number = {1, 2, 3, 3, 5}
print(number)   # 1, 2, 3, 5

# 요소 추가 및 제거
number.add(5)
print(number)
number.remove(3)
print(number)

# 집합 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 교집합: &
print(set1 & set2)

# 합집합: |
print(set1 | set2)

# 차집합: -
print(set1 - set2)

# set -> 산술연산자 지원 X
# 집합자료형 -> 계산을 위한 것이 아닌 집합 연산을 위해 설계
print([1, 2] + [3, 4])
# print({1, 2} + {3, 4})    # TypeError