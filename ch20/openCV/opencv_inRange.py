# opencv_inRange.py

import cv2
import numpy as np

# 이미지 파일 읽기 
image = cv2.imread("/Users/min/Code/rokey/py_work/ch20/openCV/aespa.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 녹색만 추출
green_lower = np.array([35, 100, 100]) 
green_upper = np.array([85, 255, 255])

# 이미지에 녹색이 없어서 다 검은색으로 나오네...
mask = cv2.inRange(hsv, green_lower, green_upper)

result = cv2.bitwise_and(image, image, mask = mask)


cv2.imshow('loaded Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()