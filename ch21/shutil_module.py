# shutil_module.py

import shutil
import os

path = r"/Users/min/Code/rokey/py_work/ch21/manage_file"

# 원본 파일 생성
src_file = f"{path}/original.txt"

with open(src_file, 'w') as f:
    f.write("This is for test. ")

# 1. 파일 복사
# copy()로 파일 복사
copyfile = f"{path}/copy.txt"
if not os.path.exists(copyfile):
    shutil.copy(src_file, copyfile)

copyfile2 = f"{path}/copy2.txt"
if not os.path.exists(copyfile2):
    shutil.copy(src_file, copyfile2)

# 2. 디렉토리 복사
# 디렉토리 생성
src = f"{path}/test_dir"
dst = f"{path}/copied_test_dir"

if not os.path.exists(src):
    os.mkdir(src)
    
if not os.path.exists(dst):
    os.mkdir(dst)

shutil.copytree(src, dst)

# 3. 파일 및 디렉토리 이동
src = f"{path}/test_dir"
dst = f"{path}/copied_test_dir"

shutil.move(src, dst)

# 3. 파일 및 디렉토리 삭제
dir1 = f"{path}/test_dir"
dir2 = f"{path}/copied_test_dir"
# file1 = f"{path}/copy.txt"
# file2 = f"{path}/copy.txt"

shutil.rmtree(dir1)
shutil.rmtree(dir2)