# 8. Scikit-learn을 사용하여 로지스틱 회귀 모델을 학습시키세요.
# 데이터:
# X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# 새로운 입력 [[4.5], [6.5]]에 대한 예측 결과를 출력하세요.

# from sklearn import svm
# from sklearn import metrics

# clf= svm.SVC()

# X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# clf.fit(X, y)
# pre = clf.predict([[4.5], [6.5]])
# print(pre)

# from sklearn.linear_model import LogisticRegression

# # 모델 생성
# clf = LogisticRegression()

# # 데이터
# X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# # 학습
# clf.fit(X, y)

# # 예측
# pre = clf.predict([[4.5], [6.5]])

# # 출력
# print(pre)

# 6. Statsmodels를 사용하여 단순 선형 회귀 모델을 구축하세요.
# x 값이 [1, 2, 3, 4, 5], y 값이 [2, 4, 6, 8, 10]일 때, 선형 회귀를 적용하여 회귀 계수(기울기, 절편)를 출력하세요.

# import statsmodels.api as sm

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# x = sm.add_constant(x)

# model = sm.OLS(y, x).fit()
# print(model)

# 7. 앞서 작성한 선형 회귀 모델의 데이터를 활용하여 다음과 같은 
# 결과 그래프를 생성하는 산점도와 선형회귀 모델의 선 그래프를 그리시오.

import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# 데이터
# X = [[1], [2], [3], [4], [5]]
X = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 선형 회귀 모델 생성 및 학습
# model = LinearRegression()
# model.fit(X, y)

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()


# 예측값 생성
y_pred = model.predict(X)

# 산점도
plt.scatter(X, y)

# 선형 회귀 직선
plt.plot(X, y_pred, color='red')

# 제목 및 축 이름
plt.title("Linear Regression")
plt.xlabel("x")
plt.ylabel("y")

# 그래프 출력
plt.show()