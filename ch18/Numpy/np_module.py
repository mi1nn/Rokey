# np_module.py

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))   # numpy.ndarray

print(arr.shape)   # (5,)
print(arr.dtype)   # int64

print('----------- 0으로 초기화된 배열 -----------')
# ones/zeros는 수치 계산 최적화를 위해 float64가 기본
zeros = np.zeros([3, 3])
print(zeros)
print(type(zeros))   # numpy.ndarray

print('----------- 1로 초기화된 배열 -----------')
ones = np.ones([2, 4])
print(ones)
print(ones.shape)   # (2, 4)
print(ones.dtype)   # float64

print('--------- 특정 값으로 초기화된 배열 ---------')
full = np.full((2, 2), 7, dtype = float)
print(full)

print('--------------- 단위 행렬 ---------------')
identity1 = np.eye(2, 3)  # 단위 행렬은 아님. 2 by 3 이라서
print(identity1)
print()

identity2 = np.eye(3)   # 대각 행렬
print(identity2)
print()

print('--------------- 난수 배열 ---------------')
# 0dㅣ상 1 미만 범위의 실수 난수 생성
random = np.random.rand(3, 3)   
print(random)
print(random.shape)
print(random.dtype)
print()

randint = np.random.randint(1, 10, (3, 3))  # 1 이상 10 미만 정수 난수 배열
print(randint)
print(randint.shape)
print(randint.dtype)

print('------------ 기본 산술 연산 ------------')
# 배열 연산
arr = np.array([1, 2, 3, 4, 5])
print(arr + 5)
print(arr * 2)

print('--------------- 통계 함수 ---------------')
print(arr.sum())
print(arr.mean())
print(arr.min())
print(arr.max())

print('------------- 브로드 캐스팅 --------------')
arr1 = np.array([1, 2, 3])
print(arr1)
print(arr1.shape)
print()

arr2 = np.array([[1], [2], [3]])
print(arr2)
print(arr2.shape)
print()

result = arr1 + arr2 
print(result)
print(result.shape)
print()

print('--------------- 행렬 곱 ---------------')
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)
print(result)
result2 = matrix1 * matrix2
print(result2)
print()

print('------------- 기본 인덱싱 --------------')
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])

arr4 = np.array([[1, 2, 3], 
                [3, 4, 5]])
print(arr4[1, 2])
print()

print('--------------- 슬라이싱 ---------------')
print(arr4[0, :])
print(arr4[:, 1])
print()

print('------------- 조건부 연산 --------------')
arr = np.array([1, 2, 3, 4, 5])
filtered = arr[arr > 3]
print(filtered)
print()

import pandas as pd
df = pd.DataFrame(arr, columns = ["Value"])
print(df)
print(type(df))   # pandas.DataFrame