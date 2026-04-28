# ttry_except2.py

print("try-except2")

path = r"/Users/min/Code/rokey/py_work/ch13/exception/myfile.txt"

#FileNotFoundError
# f = open(path)   # mode 기본값 read "r"
# f.write("Hello")
# f = open(path, "w")

# io.UnsupportedError
# s = f.readline()

# ValueError
# i = int(s.strip())

try:
    f = open(path)
    s = f.readline()
    i = int(s.strip())   # 공백제거
except OSError:
    print("OSError")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다. ")
except ValueError as e:
    print("정수형으로 변환할 수 없스니다. ")
    print(e)
except Exception as err:
    print("Exception", err)  # 예외관련 정보 표시
finally:
    print("Finally")    

# BaseException
#     Exception
#         OSError
#         ValueError
#         ...


print("program exit")