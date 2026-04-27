# file_readline
# .py

# f = open(r"ch12/file1.txt", "r")   # 윈도우인 경우, encoding 필수
f = open(r"ch12/file1.txt", "r", encoding = "utf-8")

# line1 = f.readline(5)  # 5글자까지만 읽기
# line2 = f.readline()
# line3 = f.readline()


# 특정 줄만 읽어서 출력
for i, line in enumerate(f, start = 1):
    if i == 3:
        print(i, line)

# print(line1) 
# print(line2) 
# print(line3)

f.close()