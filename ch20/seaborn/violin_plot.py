# violin_ploy.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 모드
iris = sns.load_dataset("iris")


# 3. 그래프 표시
sns.violinplot(data = iris, 
                x = "species", 
                y = "sepal_length", 
                inner = "quart")   

plt.title("Violin Plot Example")
plt.show()

# inner = "quart"   # 사분위수 표현
# None -> 내부 표시 안함
# point -> 각 데이터 그쯤의 평균값을 점으로 표시
# box -> 박스 플롯 모양
# stick -> 각 데이터 포인터를 세로선 표시