# opencv_resize.py

import cv2

image = cv2.imread("/Users/min/Code/rokey/py_work/ch20/openCV/fresh_morning-mind-10152727_1920.png")

resized = cv2.resize(image, (300, 300))   # 단위: 픽셀(pixel)

cv2.imshow("Loaded Image", resized)
cv2.waitKey(0)   # 0: 무한 대기
cv2.destroyAllWindows()
