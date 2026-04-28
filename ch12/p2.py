# p2.py

path = r"ch12/account1.txt"
mode = "r"  # 읽기 모드
encodings = "utf-8"

f = open(path, mode, encoding = encodings)

lines = f.readlines()  # 리스트

# 반복문으로 각 라인 확인
accountlist = []
for line in lines:
    # print(line[-15:])
    # accountlist.append(line[-15:].strip())
    lineList = line.split()
    print(lineList[1])
    
# print(accountlist)

# 문자열 일부 내용 가져오기 (슬라이싱 또는 split())