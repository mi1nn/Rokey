# for1.py

# for 변수 in 리스트:
#     코드블럭

for num in [0, 1, 2]:
    print(num)
    print('hi')

characters = ['앨리스', '도도새', '3월토끼']

for character in characters:
    print(character)

print('------------------------')

for letter in '도둑고양이':
    print(letter)

print('------------------------')

nums = [0, 1, 2]

for num in nums:
    print(num)
    print(nums)

print('------------------------')

# 문제 1
for num in [3, 1, 2]: 
    print(num)

print('------------------------')

# 문제 2

clovers = ['클로버1', '클로버2', '클로버3']
for clover in clovers:
    print(clover)

print('------------------------')

# 문제3

for i in range(3):
    print(clovers[i])
    
print('------------------------')

# 문제4
count = 0 
while count < 3:
    print(count)
    count = count + 1
    
print('------------------------')

# 문제5
count = 1
while count < 4:
    count += 1
    print(count)

print('------------------------')

# 문제6
count = 0 
while count <= 5:
    if count % 2 != 0:
        print(count)
    count += 1
    
print('------------------------')

# # 문제7
# price = 0
# while price != -1:
#     price = int(input('가격을 입력하세요 (종료: -1): '))
#     if price > 10000:
#         print('너무 비싸요. ')
#     elif price > 5000:
#         print('괜찮은 가격이네요. ')
#     elif price > 0:
#         print('정말 싸요. ')

print('------------------------')

# 문제8 구구단 1단
for i in range(1, 10):
    print("1 *", i, "=", i  * 1)
