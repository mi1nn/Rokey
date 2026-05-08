# plt_module.py

import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams["font.family"] = "AppleGothic"  # Mac 사용자
# plt.rcParams["font.family"] = "Malgun Gothic" 

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]

# plt.plot(x, y)
# plt.title("Line Plot")
# plt.xlabel("x-축")
# plt.ylabel("y-axis")
# # plt.show()

# print('-------------------------')
# # 막대 그래프
# categories = ["A", "B", "C", "D"]
# values = [3, 7, 8, 5]
# plt.bar(categories, values)
# plt.title("Bar Chart")
# # plt.show()

# print('-------------------------')
# # 히스토그램

# data = [1, 2,2, 3, 3, 3, 4, 4, 4, 4]
# plt.hist(data, bins = 4, color = "skyblue", edgecolor = "black")
# plt.title("Histogram")
# plt.show()

# print('-------------------------')
# # Scatter Plot(산점도)

# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
# plt.scatter(x, y, color="green")
# plt.title("Scatter Plot")
# plt.show()

# print('-------------------------')
# # Pie Chart (파이 차트, 원 그래프)

# sizes = [15, 30, 45, 10]
# labels = ["Group A", "Group B", "Group C", "Group D"]
# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
# plt.title("Pie Chart")
# plt.show()

# %: 포맷 시작
# 1: 전체 최소 자릿수
# .1: 소수점 자릿수
# f: 실수(float) 형식
## %%: 실제 % 문자 출력

# print('-------------------------')
# # Box Plot (박스 플롯)

# data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8]
# # data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8, 50]
# # 이상치(outlier): 대부분의 데이터 패턴에서 크게 벗어난 값 (50)
# plt.boxplot(data)
# plt.title("Box Plot")
# plt.show()

# print('-------------------------')
# # Box Plot (박스 플롯)

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 40]

# # plt.plot(x, y, color = "red", linestyle = "-", marker = "^")
# plt.plot(x, y, "k^:")   # 축약형
# plt.show()

# # linestyle: "-", "--", ":", "-.", ...
# # marker: ".", ",", "o", "^", "v", ...

# print('-------------------------')

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 40]
# plt.plot(x, y, "k^:")  # black, triangle, dotted
# plt.xlim(0, 5)
# plt.ylim(0, 40)
# plt.xticks(range(1, 5))
# plt.yticks(range(0, 41, 10))
# plt.show()

# print('-------------------------')

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# x1 = [1, 2, 3, 4]
# y2 = [3, 5, 9, 7]
# plt.plot(x, y, label="Data 1")
# plt.plot(x1, y2, label="Data 2")
# plt.legend(loc="upper left")
# plt.savefig("ch18/Matplotlib/my_plot.png")
# plt.show()

print('-------------------------')
# Subplot 활용 1

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# fig: 전체 그래프형
# axs: 각 subplot (그래프 영역)
 
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].bar(categories, values)
axs[1, 0].scatter(x, y)
axs[1, 1].hist(data)
fig.suptitle("전체 그래프 제목")
plt.tight_layout()
plt.show()