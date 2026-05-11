# opencv_detectedge.py

import cv2

image = cv2.imread("/Users/min/Code/rokey/py_work/ch20/openCV/fresh_morning-mind-10152727_1920.png")

edge = cv2.Canny(image, threshold1 = 100, threshold2 = 200)

cv2.imshow("Loaded Image", edge)
cv2.waitKey(0)   # 0: 무한 대기
cv2.destroyAllWindows()

# 엣지 (edge): 이미지에서 밝기(또는 색)가 갑자기 변하는 경계