# generator1.py

# 제너레이터 생성방법 1: yield 사용
def mygen():
    for i in range(1, 100):
        result = i * i
        yield result
        
gen = mygen()
print(next(gen))
print(next(gen))
print("line No.: ", gen.gi_frame.f_lineno)
print(next(gen))
print("line No.: ", gen.gi_frame.f_lineno)

for item in gen:
    print(item)
    
print(next(gen))
# print(gen)
# print(gen)