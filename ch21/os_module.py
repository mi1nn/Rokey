# os_module.py

import os

# 1. 현재 작업 디렉토리 확인 및 변경
print(f"현재 작업 디렉토리: {os.getcwd()}")

# 2. 작업 디렉토리 변경
os.chdir(r"/Users/min/Code/rokey/py_work/ch21/manage_file")

# 변경된 작업 디렉토리 확인
print(f"변경 작업 디렉토리: {os.getcwd()}")

# 전체 디렉토리의 파일 및 폴더 목록 출력
print(f"디렉토리 목록: {os.listdir(".")}")

# 3. 디렉토리 생성 및 출력
# os.mkdir("test_dir")
# os.rmdir("test_dir")
print(f"디렉토리 목록: {os.listdir(".")}")

# 4. 파일 존재 여부 확인
if os.path.exists("file.txt"):
    print("파일 존재")
    
# 5. 파일 및 디렉토리 경로 다루기
folder = os.getcwd()
print(folder)

# 경로 합치기
print(os.path.join(folder, "file.txt"))

# 파일명만 추출
print(os.path.basename(f"{folder}/file.txt"))

# 디렉토리 경로 추출
print(os.path.dirname(f"{folder}/file.txt"))