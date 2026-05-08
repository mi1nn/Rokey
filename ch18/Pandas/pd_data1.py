# pd_data1.py

import pandas as pd

# 데이터 조작
print('-----------------')
# 딕셔너리 활용 생성

data = {
    "ID": [1, 2, 3], 
    "NAME": ["Alice", "Bob", "Charlie"],
    "AGE": [30, 25, 35]
}

df = pd.DataFrame(data)
print(df)

print('------------ 열 선택 ------------')
print(df['NAME'])
print(type(df['NAME']))   # pandas.Series
print(df['AGE'])

print('----------- 조건 필터링 -----------')
print(df['AGE'] > 30)
print(type(df['AGE'] > 30))   # pandas.Series

print(df[df['AGE'] > 30])
print(type(df[df['AGE'] > 30]))   # pandas.DataFrame

print('----------- 데이터 정렬 -----------')
# 오름차순 / 내림차순

sorted_df_asc = df.sort_values(by = "AGE")  # 오름차순
sorted_df_dsc = df.sort_values(by = "AGE", ascending = False)  # 내림차순
print(sorted_df_asc)
print(sorted_df_dsc)

print('--------- 데이터 추가 및 삭제 ---------')
# 열 추가
df["SALARY"] = [5000, 6000, 7000]
print(df)
print()

# 행 추가
# df.loc[3] = [4, "David", 40, 8000]
df.loc[len(df)] = [4, "David", 40, 8000]
print(df)

print('------------ 행 삭제 ------------')
df = df.drop(1)
print(df)
# 행 번호 주의
print(len(df))

# df.loc[len(df)] = [5, "Eva", 50, 9000]  # 3번 인덱스에 오버라이딩 (덮어씌워짐)
# print(df)

print('----------- 인덱스 재정렬 -----------')
# df1 = df.reset_index()    # 새로운 index라는 열이 생기면서 이전 인덱스 번호를 저장해둠
df1 = df.reset_index(drop = True)
print(df1)

print('----------- 데이터 연결 -----------')

data2 = {
    "ID": [5, 6],
    "NAME": ['EVE', 'Frank'],
    "AGE": [28, 33]
}

df2 = pd.DataFrame(data2)
print(df2)

concated = pd.concat([df, df2], ignore_index = True)  # ignore_index -> 기존 인덱스 번호 무시하고 정렬
print(concated)

print('----------- 데이터 병합 -----------')
# 병합시 기준열 필요

data3 = {
    "ID": [1, 2, 3, 4, 5, 6],
    "DEPARTMENT": ["HR", "Engineering", "Sales", "R&D", "Finance", "Planning"]
}
df3 = pd.DataFrame(data3)
print(df3)
print()

merged = pd.merge(concated, df3)
print(merged)

print('----------- 결측치 처리 -----------')
print(merged.isnull())
print()
print(merged.isnull().sum())  # 각 열의 NaN 값 개수 확인
print()

# 결측치 체우기
meanVal = merged["SALARY"].mean()  # SALARY의 평균
print(meanVal)
print()

merged["SALARY"] = merged["SALARY"].fillna(meanVal)  # NaN을 평균으로 채운다
print(merged)

print('----------------------------------')
# merge 데이터가 모두 체워져 있어야 가능
print(merged["SALARY"].count())
print(merged["SALARY"].std())
print(merged["SALARY"].min())
print(merged["SALARY"].max())
print(merged["SALARY"].quantile(0.25))
print(merged["SALARY"].quantile(0.50))
print(merged["SALARY"].quantile(0.75))
print()

# 특정 위치값 수정
merged.loc[4, "SALARY"] = 8500
print(merged)

print('--------- 중복 데이터 처리 ---------')
data1 = {
    "ID": [1, 3],
    "NAME": ["Alice", "Charlie"],
    "AGE": [30, 35], 
    "SALARY": [5000, 7000], 
    "DEPARTMENT": ["HR", "Sales"]
}

df1 = pd.DataFrame(data1)
df1 = pd.concat([merged, df1])

print(df1)
print(df1.duplicated())

df1_1 = df1.drop_duplicates()
print(df1_1)