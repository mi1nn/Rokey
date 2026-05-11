# histoplot.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 모드
iris = sns.load_dataset("iris")

# 2. 기본 스타일 설정
sns.set_theme(style = "darkgrid")
sns.set_palette("pastel")

# 3. 그래프 표시
sns.histplot(data = iris, 
                x = "sepal_length", 
                # y = "sepal_width", 
                hue = "species", 
                kde = True)   # 분포 곡선

plt.title("Histogram Example")
plt.show()
