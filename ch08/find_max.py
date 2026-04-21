# find_max.py

# 최대값 찾기
ca = [10, 17, 13, 11]

max = ca[0]
if max < ca[1]:
    max = ca[1]
if max < ca[2]:
    max = ca[2]
if max < ca[3]:
    max = ca[3]
print(max)

print('----------------------')

ca = [10, 17, 13, 11]
max = ca[0]

for i in range(1, 4, 1):
    if max < ca[i]:
        max = ca[i]

print(max)

print('----------------------')

ca = [10, 17, 13, 11]
max = ca[0]

for i in ca:
    if max < i:
        max = i

print(max)
