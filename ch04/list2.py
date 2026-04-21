# list2.py

# 값 추가하기
# 리스트명.함수()

listc = []
print(listc)
print(type(listc))

print('--------------------')

listc.append(300)
print(listc)
listc.append('파이썬')
print(listc)
listc.append(3.7)
print(listc)

print('----------------------')

# 값 제거하기
# 리스트명.remove(제거할 값)

subject = ['국어', '수학', '영어', '국사']
print(subject)
subject.append('영어')
print(subject)
subject.remove('영어')
print(subject)

print('----------------------')

clover = ['클로버1', '클로버2', '클로버3']
print(clover[1])

del clover[1]
print(clover)

print('----------------------')

clover = ['클로버1', '클로버2', '클로버3']

clover.insert(1, '클로버4')
print(clover)

# 클로버5를 리스트 맨 앞에 추가
clover.insert(0, '클로버5')
print(clover)

clover.insert(6, '클로버7')  # 4번 인덱스까지 있지만 6번에 추가하면, 5번에 추가된다. 
print(clover)

print('--------------------------')

# 여럭러 값 추가 
clover.extend(['클로버8', '클로버0'])
print(clover)