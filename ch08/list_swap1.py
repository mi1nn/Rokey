# list_swap1.py

ca = [10, 11]
print("ca[0]: ", ca[0], end = " ")
print("ca[1]: ", ca[1])

temp = ca[0]
ca[0] = ca[1]
ca[1] = temp
print("ca[0]: ", ca[0], end = " ")
print("ca[1]: ", ca[1])

print()
print('-------------------------')

def funca(na, nb):
    temp = na
    na = nb
    nb = temp
    
ca = [10, 11]
print("ca[0]: ", ca[0], end = " ")
print("ca[1]: ", ca[1])

funca(ca[0], ca[1])
print("ca[0]: ", ca[0], end = " ")
print("ca[1]: ", ca[1])

print()
print('-------------------------')

ca = [10, 11]
cb = ca
print("ca: ", ca)
print("cb: ", cb)

# ca를 참조하고 있는 cb를 변경하며, ca값도 같이 변경 / 같은 메모리 주소의 값을 변경해서
temp = cb[0]
cb[0] = cb[1]
cb[1] = temp
print("ca[0]: ", ca[0], end = " ")
print("ca[1]: ", ca[1])
print("cb[0]: ", cb[0], end = " ")
print("cb[1]: ", cb[1])

print()
print('-------------------')

def funcb(cb):
    print("리스트 cb주소: ", id(cb))
    temp = cb[0]
    cb[0] = cb[1]
    cb[1] = temp
    
ca = [10, 11]
print("ca[0]: ", ca[0], end = " ")
print("ca[1]: ", ca[1])

funcb(ca)
print("리스트 ca 주소: ", id(ca))
print("ca[0]: ", ca[0], end = " ")
print("ca[1]: ", ca[1])

