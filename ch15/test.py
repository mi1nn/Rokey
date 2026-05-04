# # 7. 주어진 리스트에서 next() 함수를 사용하여 각 요소를 하나씩 출력하세요. 
# # StopIteration 예외를 처리하여 출력이 끝날 때까지 반복되도록 하세요.

# fruits = ["apple", "banana", "cherry"]

# it = iter(fruits)
# print(next(it))
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break
    
# 8. 0부터 9까지의 숫자를 이터레이터로 순회하며,
# 각 숫자의 제곱을 출력하는 프로그램을 작성하세요.

# num = list(range(10))
# it = map(lambda x: x ** 2, num)
# print(type(it))
# for n in it: 
#     print(n)

# 9. 0부터 10까지의 숫자 중 짝수만 출력하는 프로그램을 작성하세요. 
# 이때, 이터레이터를 사용해야 합니다.

# num = list(range(11))
# it = filter(lambda x: x % 2 == 0, num)

# for n in it: 
#     print(n)


# 10. MyRange라는 이름의 클래스를 만들어, range()와 
# 같은 기능을 하는 이터레이터를 작성하세요. 
# start, stop, step을 인자로 받아서 동작해야 하며, 
# __iter__()와 __next__() 메서드를 구현해야 합니다.

# class MyRange:
    
#     def __init__(self, start, stop = None, step = 1):
#         if stop is None:
#             self.start = 0 
#             self.stop = start
#         else:
#             self.start = start 
#             self.stop = stop
#         self.step = step
#         self.current = self.start

#     def __iter__(self):
#         return self
    
#     def __next__(self): 
#         if (self.step > 0 and self.current >= self.stop) or \
#             (self.step < 0 and self.current <= self.stop):
#             raise StopIteration
        
#         value = self.current
#         self.current += self.step
#         return value
    
# for i in MyRange(1, 10, 2):
#     print(i)


# 문제 2) 제너레이터 함수를 만들어 1부터 n까지 숫자의 제곱을 
# 생성하는 프로그램을 작성하시오.

num = list(range(10))
square = map(lambda x: x ** 2, num)
for n in square:
    print(n)

