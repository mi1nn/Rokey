# opencv_blur.py

import cv2

image = cv2.imread("/Users/min/Code/rokey/py_work/ch20/openCV/fresh_morning-mind-10152727_1920.png")

blurred = cv2.GaussianBlur(image, (15, 15), 0)

# 블러 함수에서 커널 크기는 홀수
# 홀수 크기 커널이어야 중앙 픽셀에 존재하여 대칭적 처리 가능
# 픽셀 주변 값 평균/가중평균 통으로 처리

cv2.imshow('loaded Image', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 시그마: 퍼짐 정도
# sigmaX가 크면 더 넓게 퍼짐 -> 강한 blur