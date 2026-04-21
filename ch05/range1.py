# range1.py

# range(정수)
# range(시작정수, 끝정수)
# range(시작정수, 끝정수, 증감정수)

a = range(10)

print(a)  # range(0, 10)
print(list(a))

print('----------------------')

print(range(10))
print(list(range(10)))

print('------------------------')

print(range(2, 9, 2))
print(list(range(2, 9, 2)))

print('------------------------')

for num in range(3):
    print('Hello', num)
    num += 1
    print(num)

print()

for num in range(1, 5):
    print('Hello', num)

print()

for num in range(0, 5, 2):
    print('Hello', num)

# Tuple
fruits = ('사과', '배', '바나나', '망고')
for fruit in fruits:
    print(fruit)

