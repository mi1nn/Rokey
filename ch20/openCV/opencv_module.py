# opencv_module.py

import cv2

image = cv2.imread("/Users/min/Code/rokey/py_work/ch20/openCV/fresh_morning-mind-10152727_1920.png")


cv2.imshow('loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()