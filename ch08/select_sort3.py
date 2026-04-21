# select_sort3.py

# 선택정렬
# fselsort 함수로 정의 및 호출

def fselsort(a):
    
    for i in range(0, len(a) - 1):
        
        min_x = i     # 0, 1, 2, 3
        min_a = a[min_x]    # a[0], a[1], a[2], a[3] 
        
        for j in range(i + 1, len(a)):   
            if min_a > a[j]:   # a[0] > a[1], a[2], a[3], a[4]
                min_a = a[j]   
                min_x = j
        
        temp = a[i]
        a[i] = a[min_x]
        a[min_x] = temp
    
    return a


a = [21, 10, 11, 15, 13]
print(fselsort(a))

b = [13, 45, 65, 1, 45, 98, 107]
print(fselsort(b))


## GPT 추천
# def sort_func(a):
#     for i in range(len(a) - 1):
#         min_x = i
#         for j in range(i + 1, len(a)):
#             if a[min_x] > a[j]:
#                 min_x = j
#         a[i], a[min_x] = a[min_x], a[i]
#     return a

## 에러 원인 -> x를 매개변수로 받고 반환하지만, 실행은 a로 동작해서 에러 발생
# def fselsort(x):
    
    # for i in range(0, len(x) - 1):
        
    #     min_x = i     # 0, 1, 2, 3
    #     min_a = a[min_x]    # a[0], a[1], a[2], a[3] 
        
    #     for j in range(i + 1, len(x)):   
    #         if min_a > a[j]:   # a[0] > a[1], a[2], a[3], a[4]
    #             min_a = a[j]   
    #             min_x = j
        
    #     temp = a[i]
    #     a[i] = a[min_x]
    #     a[min_x] = temp
    
    # return x
