# try:
#     x = int("abc")
# except ValueError:
#     print("ValueError occurred!")
# finally:
#     print("Execution finished.")

# try:
#     raise KeyError
# except KeyError:
#     print("Key is missing!")

# add = lambda x, y: x + y
# print(add(3, 7))

# per = ["10.31", "", "8.00"]

# P = []

# for i in per:
#     try:
#         value = float(i)
#     except ValueError:
#         value = 0.0
    
#     print(value)
#     P.append(value)

# print(P)

# numbers = [10, 20, 30]

# try:
#     x = int(input("Insert number: "))
#     print(numbers[x])
# except IndexError:
#     print("Wrong Index")
# except ValueError:
#     print("Put the number in")

# try:
#     square = lambda x: x ** 2
#     it = int(input("insert number: "))
#     result = square(it)
#     print(result)
# except ValueError:
#     print("올바른 숫자를 입력하세요!")
# except TypeError:
#     print("올바른 숫자를 입력하세요!")

num = [10, 20, 30, 40, 50]
# try:
#     result = []
#     square = lambda x: x ** 2
#     for i in num:
#         result.append(square(num))
#         print(result)
# except BaseException:
#     pass
# #     print("Somethings Wrong!")

result = []
square = lambda x: x ** 2
for i in range(len(num)):
    result.append(square(num[i]))
print(result)