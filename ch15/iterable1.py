# iterable1.py

a = [1, 2, 3]
# next(a)   # TypeError

# 'list' object is not an iterator
# 리스트는 반복가능 하지만(iterable) 이터레이터(iterator)는 아님

# 이터레이터 생성 방법1: iter() 함수 사용
iter_a = iter(a)
print(type(iter_a))   # class 'list_iterator'

# print(next(iter_a))   # 1
# print(next(iter_a))   # 2
# print(next(iter_a))   # 3
# print(next(iter_a))   # StopIteration

for i in iter_a:
    print(i)
    
for i in iter_a:
    print(i)
    
print(next(iter_a))   # StopIteration