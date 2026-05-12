# 1_managefile.py

import os
import shutil

# 1. 특정 폴더에서 모든 .txt 파일을 검색하여 리스트로 반환하는 함수를 작성하시오.
def Find(path):
    
    list = []
    
    result = os.listdir(path)
    
    for file in result:
    
        if file[-4:] == ".txt":
            list.append(file)
    
    return list

path = r"/Users/min/Code/rokey/py_work/ch21/manage_file"

print(f"txt 파일: {Find(path)}")


