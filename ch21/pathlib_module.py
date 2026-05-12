# pathlib_module.py

from pathlib import Path

print(Path.cwd())

print('-----------------------')
# 경로 생성 및 조작
folder = "/Users/min/Code/rokey/py_work/ch21/classify_file"
path = Path(folder)
print(path)

# '/' 생산자는 경로 결합 연산자로, 
# pathlib.Path 객체에서 지원
print(path / "file.txt")

# 3. 디렉토리 및 파일 존재 여부 확인
file = "/Users/min/Code/rokey/py_work/ch21/classify_file/file.txt"
path = Path(file)

print(path.exists())   # 존재 여부 
print(path.is_file())  # 존재 및 파일 여부 
print(path.is_dir())   # 존재 및 디렉토리 여부

print('-----------------------')
# 디렉토리 생성 및 삭데
new_folder = "/Users/min/Code/rokey/py_work/ch21/classify_file/new_folder"
path = Path(new_folder)
path.mkdir(exist_ok=True)
path.rmdir()

print('-----------------------')
# 파일 생성 및 삭제
file = "/Users/min/Code/rokey/py_work/ch21/classify_file/file.txt"
file_path = Path(file)
file_path.touch()   # 빈 파일 생성
file_path.unlink()   # 파일 삭제
