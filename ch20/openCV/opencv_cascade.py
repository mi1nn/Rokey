# opencv_cascade.py

import cv2
import matplotlib.pyplot as plt

# 1. 이미지 파일 읽기
image = cv2.imread("/Users/min/Code/rokey/py_work/ch20/openCV/aespa.jpg")

# 2. 얼굴 검출을 위한 모델 확인
# 'haarcascade_eye.xml'
face_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

# 3. 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. 케스케이드 분류기 생성
face_cascade = cv2.CascadeClassifier(face_path)

# 5. 얼굴 검출 수행
faces = face_cascade.detectMultiScale(gray,   # 입력 이미지 
                                      scaleFactor = 1.1,   # 이미지 크기를 줄여가며 검출 (1.1배씩 감소 = 10% 씩 줄여가며 검사)
                                      minNeighbors = 5,   # 객체로 인지되기 위한 최소 중복 검출 수
                                      minSize = (30, 30))  # 검출할 객체의 최소 크기

print(faces)    # [x, y, w, h]

# 6. 검출된 얼굴 주위에 사각형 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 이미지 창에 표시 
cv2.imshow('loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()