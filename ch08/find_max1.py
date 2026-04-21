# find_max1.py

u = [5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    
    max = a    

    if max < b:
        max = b
    if max < c:    ## elif로 작성할 경우, 해당 조건이 참이면 뒤를 검사하지 않는다. (처음 True에서 종료)
        max = c
    if max < d:
        max = d
    if max < e:
        max = e
    
    return max

max = fmax(u[0], u[1], u[2], u[3], u[4])
print("최대값: ", max)

print()
print('------------------------------')

def fmax2(a, b, c, d, e):
    
    fu = [a, b, c, d, e]
    max = fu[0]    

    for i in range(1, 5, 1):
        if max < fu[i]:
            max = fu[i]
    
    return max

max = fmax2(u[0], u[1], u[2], u[3], u[4])
print("최대값: ", max)

print()
print('------------------------------')

def fmax3(a, b, c, d, e):
    
    fu = [a, b, c, d, e]
    max = fu[0]    

    for i in fu:
        if max < i:
            max = i
    
    return max

max = fmax3(u[0], u[1], u[2], u[3], u[4])
print("최대값: ", max)

print()
print('------------------------------')

def fmax4(a, b, c, d, e):
    
    fu = []
    fu.append(a)
    fu.append(b)
    fu.append(c)
    fu.append(d)
    fu.append(e)
    
    max = fu[0]

    for i in fu:
        if max < i:
            max = i
    
    return max

max = fmax4(u[0], u[1], u[2], u[3], u[4])
print("최대값: ", max)

print()
print('------------------------------')

def fmax5(fu):
    
    max = fu[0]    

    for i in fu:
        if max < i:
            max = i
    
    return max

max = fmax5(u)
print("최대값: ", max)

print()
print('------------------------------')

def fmax6(fu):
    
    max = fu[0]    

    for i in range(1, 5, 1):
        if max < fu[i]:
            max = fu[i]
    
    return max

max = fmax6(u)
print("최대값: ", max)

print()
print('------------------------------')

def fmax7(fu):
    
    max = fu[0]    

    for i in range(1, len(fu)):
        if max < fu[i]:
            max = fu[i]
    
    return max

v = [5, 4, 1, 7, 8, 12, 15, 3, 17]
max = fmax7(v)
print("최대값: ", max)