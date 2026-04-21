# dict1.py

# {'키1': '값1', '키2': '값2', '키3': '값3'}

my_dict = {}   # 빈 딕셔너리
print(my_dict)
print(type(my_dict))   # dict

my_dict2 = {
    0: 1, 
    1: -2, 
    2: 3.14
}
print(my_dict2)

my_dict3 = {
    '이름': '엘리스', 
    '나이': 12, 
    '시력': [1.0, 1.2]
}
print(my_dict3)

# 값 추가하기
my_dict3['키'] = 120
print(my_dict3)

my_dict3['성별'] = '여성'
print(my_dict3)

# 키값 조회
print(my_dict3['이름'])
print(my_dict3.get('나이'))

print('------------------------')

clover = {'나이': 27, '직업': '병사'}
print(clover)

clover['번호'] = 9
print(clover)

# 값 변경하기
clover['번호'] = 8
print(clover)

clover = {
    '나이': 37, 
    '직업': '마법사',
    '능력': {
            '체력': 70, 
            '마력': 999
           }
}
print(clover)

print('------------------------')

# 1. 이름, 나이, 성별, 원하는 데이터 1가지
# 딕셔너리 생성
# 2. 생성된 딕셔너리에 전화번호와 주소 추가
# 3. 생성된 데이터에 접근

test1 = {
    '이름': '홍길동', 
    '나이': 23, 
    '성별': '여자', 
    '키': 187
}

test1['전화번호'] = '010-1234-5667'
test1['주소'] = '국회의사당'

print(test1)
print('나이: ',test1.get('나이'))

# 한 해 지났으니 나이 더 먹어야겠지?

test1['나이'] = test1.get('나이') + 1
print('한살 더 먹은 나이: ', test1.get('나이'))

print('------------------------')

print(test1.items())

print(test1.keys())

print(test1.values())