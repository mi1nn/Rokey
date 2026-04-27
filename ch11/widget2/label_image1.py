# label_image1.py

from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import PhotoImage

# 이미지 변환 -> 외장 라이브러리 활용
#   - 라이브러리 다운로드 수행 후 설치
#   - PIL(pillow)  ->  pip install pillow

from PIL import Image

# jpg -> png
image = Image.open("/Users/min/Code/rokey/py_work/ch11/widget2/apple1.jpg")   # jpg 원본 파일
image.save("/Users/min/Code/rokey/py_work/ch11/widget2/apple1.png", format = "PNG")   # png로 변환
print("이미지가 PNG로 변환되었습니다. ")

# 1. 위젯 생성
otk = Tk()   
otk.geometry("400x300")

img1 = PhotoImage(file="/Users/min/Code/rokey/py_work/ch11/widget2/apple1.png")

img1_label = Label(otk, image = img1)
img1_label.place(x = 20, y = -20)

obtn1 = Button(otk, text = "주문")
obtn2 = Button(otk, text = "주문")
obtn3 = Button(otk, text = "주문")

obtn1.place(x = 10, y = 60)
obtn2.place(x = 140, y = 60)
obtn3.place(x = 80, y = 10)

otk.mainloop()