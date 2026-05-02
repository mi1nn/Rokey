# comprehension.py

# 리스트 컴프리헨션: 새 리스트 생성
# [표현식 for 요소 in 이터러블 if 조건]

numbers = [1, 2, 3, 4]
squared = [x ** 2 for x in numbers]
print(type(squared))
print(squared)

even_number = [x ** 2 for x in numbers if x % 2 == 0]
print(even_number)

even_number = [x ** 2 + 1 for x in numbers if x % 2 == 0]
print(even_number)

print('-----------------------------')
# 딕셔너리 컴프리헨션: 새 딕셔너리 생성
# {key: value for item in iterable if condition}

squared_d = {x: x ** 2 for x in range(5)}
print(squared_d)

even_squared_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_squared_dict)
print()

subjects = ['수리', '영어', '역사']
scores = {subject: 0 for subject in subjects}
print(scores)

print('-----------------------------')
# 제너레이터 생성 방법2
# 제너레이터 컴프리헨션: 새 제너레이터 생성
# (표현식 for 요소 in 이터러블 if 조건)

gen = (i * i for i in range(1, 10))
print(type(gen))   # generator
# print(list(gen))
print(next(gen))   # 1
for item in gen:
    print(item)
# print(next(gen))   # StopIteration
