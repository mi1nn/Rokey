# pack.py

from tkinter import Tk
from tkinter import Button

# 1. 위젯 생성
otk = Tk()  
otk.geometry("100x150+400+400")   

obtn1 = Button(otk, text = 'click me1')   
obtn2 = Button(otk, text = 'click me2')
obtn3 = Button(otk, text = 'click me3')

# 2. 위젯 배치
obtn1.pack(side = "top")
obtn2.pack(side = "right")
obtn3.pack(side = "bottom")

otk.mainloop()  
