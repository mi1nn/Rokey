# describe.py

from scipy.stats import describe

data = [1, 2, 3, 4, 5, 6, 7]
stat = describe(data)
print(stat)

# 평균(중심), 분산(퍼짐)
# 외도 (Skewness)는 분포의 비대칭 정도
# 청도 (Kurtosis)는 분포의 뾰족한 정도
