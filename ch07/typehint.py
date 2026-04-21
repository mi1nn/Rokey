# typehint.py

# def 함수명(매개변수1:데이터타임, 매개변수2:데이터타입, ...):
#     코드블럭
#     return 반환값

# 예
def add(x:int, y:float) -> float:
    return x + y

print(add(3, 10))
print(type(add(3, 10)))
print(add(3, 1.32))
print(type(add(3, 1.32)))
