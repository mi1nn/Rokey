# function_memory.py

# na = 10
# nb = 11

# pa = na
# pb = nb

# nc = pa + pb

# print(nc)

print('-----------------------')

def funca(pa, pb):
    nc = pa + pb
    return nc
na = 10 
nb = 11

nd = funca(na, nb)

# 전역스코프에서 함수스코프로 접근이 안돼서 에러가 발생
print(na, " + ", nb, " = ", nd)


