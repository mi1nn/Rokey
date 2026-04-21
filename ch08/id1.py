# id1.py

# 함수 기능: ca 리스트의 원소를 모두 더한 총합 계산
def fk(cd):
    total = 0
    for sb in range(0, 3, 1):
        total = total + cd[sb]
    cd[2] = total
    return cd

ca = [10, 20, 30]
print(ca)

cb = fk(ca)
print(ca)
print(cb)
print(type(cb))