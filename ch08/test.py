a = {
    'a': 10, 
    'b': 20, 
    'c': 30
}
print(a)

def all_sum(x):
    value = 0 
    for list, number in x.items():
        value += number
    return value
    
print(all_sum(a))

dic = {"민수": 75, "영희": 92, "철수": 88, "지연": 60}
for name, score in dic.items():
    if score >= 80:
        print(name, score)
        

# data = [64, 25, 12, 22, 11]

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#             print(min_idx)
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# print(selection_sort(data))


# 6. 리스트에서 첫 번째 짝수와 마지막 홀수를 찾아 서로 스왑하는 프로그램을 작성하시오.

# def swap_odd(arr):
#     temp1 = 0
#     temp2 = 0
#     # 첫번째 짝수
#     for i in arr:
#         if i % 2 ==0:
#             temp1 = i
#             return temp1
#     # 마지막 홀수
#     arr_rev = reversed(arr)
#     for j in arr_rev:
#         if j % 2 != 0:
#             temp2 = arr[j]
#             return temp2
#     # 둘이 swap
#     temp1, temp2 = temp2, temp1
    

a = [3, 6, 7, 4, 9, 10, 13]

def swap_odd1(arr):
    temp1 = 0
    temp2 = 0
    # 첫번째 짝수
    for i in range(len(arr)):
        if arr[i] % 2 ==0:
            temp1 = i
            break
    # 마지막 홀수
    for j in range(len(arr)-1, -1, -1):
        if arr[j] % 2 != 0:
            temp2 = j
            break
    # 둘이 swap
    arr[temp1], arr[temp2] = arr[temp2], arr[temp1]
    return arr
    
    

print(swap_odd1(a))

