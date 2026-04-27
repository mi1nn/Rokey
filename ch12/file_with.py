# file_with.py

# 자동 닫기 처리
# with open(파일경로, 모드, 인코딩) as 파일객체:
#     코드블럭

path = r"ch12/file2.txt"
mode = "w"
with open(path, mode, encoding = "utf-8") as f:
    f.write("No pain No gain \n")
    f.write("노력없이는 얻는 것도 없다. ")