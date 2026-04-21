# list_swap2.py

a = [10, 11, 12, 13]
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))

print()
print('--------------------------')

a[1] = 21
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))

print()
print('--------------------------')

b = a
print("리스트 b값: ", b)
print("리스트 b값: ", id(b))

b = [30, 31, 32, 33]
print("리스트 b값: ", b)
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
print(id(b[3]))