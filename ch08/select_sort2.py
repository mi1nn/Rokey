# select_sort2.py

# 1차 목표: [10, 21, 11, 15, 13]

a = [21, 10, 11, 15, 13]
mina = a[0]  # 현 최소값
minx = 0   #현 최소값 위치(인덱스)

for i in range(1, 5, 1):
    if mina > a[i]:
        mina = a[i]
        minx = i
print(a)
print(mina, minx)

# 두 데이터를 swap
temp = a[0]
a[0] = a[minx]
a[minx] = temp

print(a)

print('---------------------------')

# 2차 목표: [10, 11, 21, 15, 13]

mina = a[1]  # 현 최소값
minx = 1   #현 최소값 위치(인덱스)

for i in range(2, 5, 1):   # 2, 3, 4
    if mina > a[i]:   # 21 > 11 => True
        mina = a[i]   #mina = 11
        minx = i   # minx = 2
print(a)
print(mina, minx)

# 두 데이터를 swap
temp = a[1]
a[1] = a[minx]
a[minx] = temp

print(a)

print('--------------------------')

# 3차 목표: [10, 11, 13, 15, 21]

mina = a[2]  # 현 최소값
minx = 2   #현 최소값 위치(인덱스)

for i in range(3, 5, 1):   # 3, 4
    if mina > a[i]:   # 21 > 13 => True
        mina = a[i]   #mina = 13
        minx = i   # minx = 4
print(a)
print(mina, minx)

# 두 데이터를 swap
temp = a[2]
a[2] = a[minx]
a[minx] = temp

print(a)

print('--------------------------')

# 4차 목표: [10, 11, 13, 15, 21]

mina = a[3]  # 현 최소값
minx = 3    #현 최소값 위치(인덱스)

for i in range(4, 5, 1):   # 3, 4
    if mina > a[i]:   # 15 > 21 => False
        mina = a[i]   #mina = 15
        minx = i   # minx = 3
print(a)
print(mina, minx)

# 바뀌는 거 없음
temp = a[3]
a[3] = a[minx]
a[minx] = temp

print(a)

