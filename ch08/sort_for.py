# sort_for.py

# 오름차순 정렬 for문

a = [21, 10, 11, 15, 13]

for i in range(0, 4):
    
    minx = i     # 0, 1, 2, 3
    mina = a[minx]    # a[0], a[1], a[2], a[3] 
    
    for j in range(i + 1, 5):   
        if mina > a[j]:   # a[0] > a[1], a[2], a[3], a[4]
            mina = a[j]   
            minx = j
    
    temp = a[i]
    a[i] = a[minx]
    a[minx] = temp
    
    print(a)


# a = [21, 10, 11, 15, 13]

# for i in range(0, 4):
    
#     minx = i  
#     mina = a[minx] 
    
#     if mina > a[i + 1]:
#         mina = a[i + 1]
#         minx = i
    
#     temp = a[i + 1]
#     a[i + 1] = a[minx]
#     a[minx] = temp
    
#     print(a)
