# find_max1.py

u = [5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    
    max = a    

    if max < b:
        max = b
    elif max < c:
        max = c
    elif max < d:
        max = d
    elif max < e:
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