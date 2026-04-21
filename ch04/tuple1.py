# tuple1.py

clovers = ('클로버1', '클로버2', '클로버3')
print(clovers[1])

# clovers[1] = '클로버4' 변경 불가

my_tuple = ()  # 빈 튜플
print(my_tuple)
print(type(my_tuple))

my_tuple2 = (1, -2, 3.14, True, 'hi', [1, 2])
print(my_tuple2)

my_tuple3 = 1, -2, 3.14, True, 'hi', [1, 2]
print(my_tuple3)
print(type(my_tuple3))

# my_tuple3[3] = False

# my_int = (1)  이건 그냥 int 타입이 되버림. 하나의 자료를 튜플로 쓰고싶음 뒤에 , 추가
my_int = (1,)
print(type(my_int))

print('------------------------')

# 형 변환: list(), tuple()
my_list3 = list(my_tuple3)
print(my_list3)
print(type(my_list3))

my_list3[3] = False
print(my_list3)

print('------------------------')

