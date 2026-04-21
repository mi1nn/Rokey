# count = 0
# while count < 3:
#     count += 1
#     if count % 2 == 0:
#         print("짝수")
#         continue
#     print(count)
    
    
# for i in range(1, 31):
#     if i % 2 == 0:
#         print(i, ":", "짝수")
#     else:
#         print(f"{i}: ", "홀수")

# def greet(name):
#     print("Hello, ",name)
# greet("Alice")


# # function을 return하지 않고, print로 끝내면 값을 화면에 출력은 하지만 값을 사용할 수 없음 -> None
# x = print(4  * 5) 
# print(x)  

# number = [1,2,3,4,5]
# print(number)

# student3 = {"나이": 22, "직업": "학생", "취미": "게임"}
# student3["도시"] = "수원"
# print(student3.keys())

# fruits = ['사과', '바나나', '파인애플', '복숭아', '포도']
# for i in fruits:
#     if i == '사과':
#         print("사과를 찾았습니다! ")

# data = [1,2,3,4,5,6]
# print(data[1:5:2])

def devide(a, b):
    try:
        res = a/b
    except ZeroDivisionError:
        return "Error"
    finally:
        print("Done", end=" ")
    return res

print(devide(10, 0))

import math
print(math.ceil(6/2))