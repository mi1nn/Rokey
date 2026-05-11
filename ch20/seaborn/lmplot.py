# sns_basic.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 모드
iris = sns.load_dataset("iris")


# 3. 그래프 표시
sns.lmplot(data = iris, 
                x = "sepal_length", 
                y = "sepal_width", 
                hue = "species", 
                height = 6)

plt.title("Linear Model Plot Example")
plt.show()

# 선 옆 반투명 음영: 회귀선의 신뢰구간 (Confidence Interval, CI)
# 실제 회귀선이 이 범위 안에 있을 가능성이 높다

