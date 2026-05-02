# map_func.py

# map(함수, 이터레이터)
# 1. 기능 / 동작: 이터레이터에 함수 적용
def square(x):
    return x ** 2

print('----------------------------')
numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = map(square, numbers)
print(list(squared_numbers))

squared_numbers = map(lambda x: x ** 2, numbers)
print(squared_numbers)
print(type(squared_numbers))
print(list(squared_numbers))