# xor.py

# import sklearn as sk

from sklearn import svm      # 알고리즘
from sklearn import metrics  # 평가
import pandas as pd          # 데이터 분석 및 조작

# 1. 데이터 수집 및 전처리
xor_data = [
    # P, Q, result
    [0, 0, 0], 
    [0, 1, 1], 
    [1, 0, 1], 
    [1, 1, 0], 
]

# 데이터 가용 -> 학습 데이터와 학습 레이블 분리
xor_df = pd.DataFrame(xor_data)
print(xor_df)
print()

# 학습 데이터 (독립변수)
data = xor_df.loc[:, 0:1]
print(data)
print()

# 학습 레이블 (종속변수)
label = xor_df.loc[:, 2]
print(label)
print()

# 데이터 학습히기
# 2. 알고리즘 선택
clf = svm.SVC()   # 알고리즘 선택  # 분류 알고리즘

# 3. 학습/훈련 -> 모델 생성
# fit (학습데이터, 학습 레이블)
# clf.fit([
#     [0, 0],  
#     [0, 1], 
#     [1, 0], 
#     [1, 1]
# ], 
#     [0, 1, 1, 0]
# )   # 학습 (모델링)

clf.fit(data, label)

# 4. 예측
pre = clf.predict([
    [0, 1],      # 1
    [1, 1]       # 0
])   # 예측 -> 답
print(pre)

# 5. 정확도 평가
# 결과 확인
ac_score = metrics.accuracy_score([1, 0], pre)
print(f"정답률: {ac_score}")
