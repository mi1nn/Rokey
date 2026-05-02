# p1.py

# 리스트를 이터레이터로 변환하고 동작확인
foods = ['김밥', '만두', '양념치킨', '족발', '피자', '쫄면', '라면']

# 이터레이터 생성방법
# 1. iter() 함수 활용
# 2. 클래스 작성
# 3. 제너레이터 생성

ifoods = iter(foods)
print(type(ifoods))

for food in foods:
    print(food)

print(next(ifoods))  # StopIteration