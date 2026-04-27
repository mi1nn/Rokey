# file_open.py

import os
# 현재 작업 디렉토리 확인
print(os.getcwd())

# "\n": 줄바꿈 (newline)
# r: raw (원형으로)
# f = open(r"/Users/min/Code/rokey/py_work/ch12/file.txt") # 절대경로
f = open(r"ch12/file_open.py")  # 상대경로 (작업 디렉토리 기준)

# f.메서드명()   # 파일객체 멤버함수
# f.변수명  # 파일객체 멤버변수

# 파일 닫기
f.close()