# try_except.py

# 예외 처리 기본 문법

# try:
#     코드블럭
# except 예외클래스:
#     코드블럭
# finally: 
#     코드블럭

# while True:
#     x = int(input("Please enter a number: "))
#     break

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again. ")
    finally: 
        print("예외 처리 후 동작하는 코드")

print("program exit")