# opencv_rotation.py

import cv2

image = cv2.imread("/Users/min/Code/rokey/py_work/ch20/openCV/fresh_morning-mind-10152727_1920.png")

print(image.shape)   # 세로, 가로, 채널 정보
(h, w) = image.shape[0:2]
center = (w/2, h/2)

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

rotated = cv2.warpAffine(image, matrix, (w, h))


cv2.imshow("Loaded Image", rotated)
cv2.waitKey(0)   # 0: 무한 대기
cv2.destroyAllWindows()
