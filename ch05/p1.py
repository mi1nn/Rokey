# 구구단 for문

# 1단
for i in range(1, 10):
    print("1 * " , i, "=", i * 1)

print('------------------------')

# 2단
for i in range(1, 10):
    print("2 * ", i, "=", i * 2)

print('------------------------')

# 3단
for i in range(1, 10):
    print("3 * ", i, "=", i * 3)

print('------------------------')

# 1 ~ 5단
for j in range(1, 6):
    for i in range(1, 10):
        print(j, " * ", i, " = ", j * i)
