# generator.py

def simple_generatoy():
    yield 'a'
    yield 'b'
    yield 'c'
    
g = simple_generatoy()
print(type(g))  # class 'generator'

print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))   # StopIteration

# 제네레이터 < 이터레이터 
# : 이터레이터가 더 큰 개념이고, 제너레이터는 그 구현 방법 중 하나 

print('----------------------------')
print(dir(g))
print('__iter__' in dir(g))   # True
print('__next__' in dir(g))   # True