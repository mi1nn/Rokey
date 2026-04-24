# grid.py

from tkinter import Tk
from tkinter import Button

# 1. 위젯 생성
otk = Tk()  
otk.geometry("100x150+400+400")   

obtn1 = Button(otk, text = 'click me1')   
obtn2 = Button(otk, text = 'click me2')
obtn3 = Button(otk, text = 'click me3')
obtn4 = Button(otk, text = 'click me4')

# 2. 위젯 배치
obtn1.grid(row = 1, column= 0)
obtn2.grid(row = 1, column= 1)
obtn3.grid(row = 0, column= 4)
obtn4.grid(row = 2, column= 3)

otk.mainloop()  
