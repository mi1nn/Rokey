# select_sort1.py

# 정렬 종류
# ca = [21, 10, 11, 15, 13]
# 오름차순 = [10, 11, 13, 15, 21]
# 내림차순 = [21, 15, 13, 11, 10]

# 1. 제일 작은 수의 인덱스 번호 찾기
# 2. 찾은 인덱스를 활용해 0번 인덱스에 최소값을 위치하기

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

#1차 목표: [10, 21, 11, 15, 13]