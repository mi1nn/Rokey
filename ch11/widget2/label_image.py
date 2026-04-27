# label_image.py

from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import PhotoImage



# 1. 위젯 생성
otk = Tk()   
otk.geometry("400x300")

img1 = PhotoImage(file="/Users/min/Code/rokey/py_work/ch11/widget2/apple.png")

img1_label = Label(otk, image = img1)
img1_label.place(x = 20, y = -20)

obtn1 = Button(otk, text = "주문")
obtn2 = Button(otk, text = "주문")
obtn3 = Button(otk, text = "주문")

obtn1.place(x = 10, y = 60)
obtn2.place(x = 140, y = 60)
obtn3.place(x = 80, y = 10)

otk.mainloop()