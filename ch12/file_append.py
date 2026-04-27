# file_append.py

path = r"ch12/file1.txt"
mode = "a"
f = open(path, mode)

for i in range(11, 21):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)

f.close()
# f = open(path, "r")
# print(f.read())
# f.close()

# "r": read 모드
# "w": write 모드
# "a": append 모드
# "r+": read + write -> 파일을 읽고 
# "w+": write + read -> 파일을 새로 
# "a+": append + read
