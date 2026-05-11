# iris.py

from sklearn.datasets import load_iris
import pandas as pd

# 1. iris 데이터셋 로드
iris = load_iris()
# print(iris)
# print('-------------')

df = pd. DataFrame(data = iris.data, 
                   columns = iris.feature_names)
df["target"] = iris.target
# print(df.head())
# print('-------------')

# 0, 1, 2 로 표현된 label을 문자열로 매핑
target_names = {
    0: iris.target_names[0],   # 'setoasa'
    1: iris.target_names[1],   # 'versicolor'
    2: iris.target_names[2],   # 'virginica'
}

df['target'] = df['target'].map(target_names)
print(df.head())
print('-------------')

from sklearn.model_selection import train_test_split

# 2. 필요한 열 추출
iris_data = df[[
    "sepal length (cm)",
    "sepal width (cm)", 
    "petal length (cm)", 
    "petal width (cm)"
]]

iris_label = df["target"]
# print(iris_data)
# print('-------------')
# print(iris_label)
# print('-------------')

# 3. 학습 전용 데이터와 테스트 전용 데이터로 나누기
train_data, test_data, train_label, test_label = \
    train_test_split(iris_data, iris_label)

print(train_data)

from sklearn import svm, metrics

# 4. 데이터 학습시키고 예측하기
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 5. 정답률 확인
ac_score = metrics.accuracy_score(test_label, pre)
print(f"정답률: {ac_score}")