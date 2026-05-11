# import pandas as pd

# df = pd.read_csv("data.csv")

# print(
#     f"Age 평균: {df['Age'].mean()}, "
#     f"최댓값: {df['Age'].max()}, "
#     f"최솟값: {df['Age'].min()}"
# )

# print(
#     f"Salary 평균: {df['Salary'].mean()}, "
#     f"최댓값: {df['Salary'].max()}, "
#     f"최솟값: {df['Salary'].min()}"
# )

# 7. 주어진 데이터프레임에서 30세 이상이면서 연봉이 60000 이상인 사람만 필터링하여 출력하세요.
# 출력 결과: 
# Name  Age  Salary
# 1   Bob   30   60000
# 3  Dave   35   70000

# import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Carol', 'Dave'],
#     'Age': [25, 30, 28, 35],
#     'Salary': [50000, 60000, 55000, 70000]
# }

# df = pd.DataFrame(data)

# result = df[(df['Age'] >= 30) & (df['Salary'] >= 60000)]

# print(result)

# 8. NumPy 배열을 사용하여 다음 연산을 수행하세요.
# 1부터 10까지의 정수 배열을 생성
# 배열의 모든 원소를 제곱
# 배열의 평균, 최댓값, 최솟값 출력

# 출력 결과:
# 원본 배열: [ 1  2  3  4  5  6  7  8  9 10]
# 제곱 배열: [  1   4   9  16  25  36  49  64  81 100]
# 평균: 38.5, 최댓값: 100, 최솟값: 1

# import numpy as np

# arr = np.arange(1, 11)

# square_arr = arr ** 2

# print("원본 배열:", arr)
# print("제곱 배열:", square_arr)

# print(
#     f"평균: {square_arr.mean()}, "
#     f"최댓값: {square_arr.max()}, "
#     f"최솟값: {square_arr.min()}"
# )

# import numpy as np

# arr = np.random.randint(1, 13, size=(3, 4))

# row_max = np.max(arr, axis=1)

# print("원본 행렬:")
# print(arr)

# print("각 행의 최댓값:", row_max)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("Line Graph")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)

plt.show()