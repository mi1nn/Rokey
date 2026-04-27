# file_write_read.py

path = r"ch12/file3.txt"
mode = "w+"
f = open(path, mode)

for i in range(11, 21):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)

f.seek(0)  # 파일 포인터 위치 재조정
print(f.read())

f.close()

# f.seek(cookie, whence)
# cookie: 파일 내 위치 상태값 (포인터 정보)
# whence 값 정리
# 0: 파일 시작
# 1: 현재 위치
# 2: 파일 끝