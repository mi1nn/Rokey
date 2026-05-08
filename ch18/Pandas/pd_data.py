# pd_data.py

import pandas as pd

# 데이터 분석
# CSV 파일 데이터 읽기

path = r'/Users/min/Code/rokey/py_work/ch18/Pandas/data.csv'  # r 쓰는 이유: \(역슬래쉬) 있을 수 있어서

# df_csv = pd.read_csv(path, header = None)
df_csv = pd.read_csv(path)

print(type(df_csv))
print(df_csv)

print('----------------------')
# Excel 파일 데이터 읽기

path2 = r"/Users/min/Code/rokey/py_work/ch18/Pandas/data.xlsx"
df_xl = pd.read_excel(path2)

print(type(df_xl))
print(df_xl)

# Excel 파일 구조
# book > sheet > cell

print('-----------------------')

# print(df_csv.head())  # 기본적으로 앞의 5개 
print(df_csv.head(3))  # 설정한 개수만큼 앞의 행 가져옴

print('-----------------------')

# print(df_csv.tail())  # 기본적으로 뒤의 5개 
print(df_csv.tail(3))  # 설정한 개수만큼 뒤의 행 가져옴

print('-----------------------')
# 데이터 요약 정보

df_csv.info()

# 객체 타입
# 행 정보
# 열 정보
# (번호, 컬럼명, 비어있지 않은 데이터 개수, 데이터타입)
# 메모리

print('------------------------')
# 기술 통계량 정보
print(df_csv.describe())

print('------------------------')
# 랜덤 샐플링 (개수 or 비율)

print(df_csv.sample(3))   # 랜덤 샘플링
print('------------------------')
print(df_csv.sample(frac = 0.5))  # 0.5는 50%, 전체 데이터에서 50% 만 샘플링
