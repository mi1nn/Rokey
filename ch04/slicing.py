# slicing.py

week = ['월', '화', '수', '목', ' 금', '토', '일']
print(week)
print(week[1:4])
print(type(week[1:4]))

# 문제1: 토/일 데이터를 출력
print(week[5:8])

# 문제2: 월 ~ 목 데이터를 출력
print(week[0:4])

print('-------------------------')
 
# 음수 인덱싱
print(week[-1])
print(week[-2])
print(week[-3])

print('-------------------------')

print(week[-3:-1])
print(week[-3:1])
print(week[1:-3])
print(week[-5:-1])

# 범위 설정 규칙: 좌 -> 우
print(week[-1:-3])  # 값이 안 나온다
print(week[7:5])  # 값이 안 나온다 
print()

# 1. 시작 인덱스 생략
print(week[:5])

# 2. 끝 인덱스 생략
print(week[2:])

# 3. 모든 인덱스 생략 -> 전체 데이터 선택
print(week[:])