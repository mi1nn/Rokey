# 6. seaborn을 사용하여 임의의 데이터를 생성하고 히스토그램을 그려보세요.
# numpy를 사용하여 평균이 50, 표준편차가 10인 정규 분포 데이터를 1000개 생성하세요.
# seaborn.histplot()을 사용하여 히스토그램을 시각화하세요.

# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt

# data = np.random.normal(loc = 50, scale = 10, size = 1000)

# sns.histplot(data, bins = 30, kde = True)

# plt.show()


# 7. seaborn을 사용하여 tips 데이터셋의 요일(day) 별 전체금액(total_bill)의 
# 박스플롯을 그려보세요. (seaborn.boxplot()을 사용하세요.)

# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")

# # sns.set_theme(style = "dark", palette = "pastel")

# sns.boxplot(data = tips, x = "total_bill", y = "tip")

# plt.show()

# 8. OpenCV를 사용하여 이미지를 불러오고 화면에 출력하세요.
# cv2.imread()로 이미지를 로드한 후, 
# cv2.imshow()를 사용하여 출력하세요.
# cv2.waitKey(0)을 사용하여 창을 닫을 수 있도록 하세요.


# import cv2

# image = cv2.imread("이미지 주소")

# cv2.imshow('loaded image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 9. OpenCV를 사용하여 컬러 이미지를 흑백(그레이스케일)으로 변환하세요.
# cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)를 사용하여 변환하세요.
# 변환된 이미지를 출력하세요.

# import cv2

# image = cv2.imread("이미지주소")

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Grayscale Image", gray)
# cv2.waitKey(0)   
# cv2.destroyAllWindows()

# 10. OpenCV의 cv2.Canny()를 사용하여 이미지의 엣지를 감지하세요.
# 엣지를 감지한 후, 결과 이미지를 출력하세요.

import cv2

image = cv2.imread("이미지 주소")

edge = cv2.Canny(image, threshold1 = 100, threshold2 = 200)

cv2.imshow("Loaded Image", edge)
cv2.waitKey(0)   
cv2.destroyAllWindows()
