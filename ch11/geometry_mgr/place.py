# place.py

from tkinter import Tk
from tkinter import Button

# 1. 위젯 생성
otk = Tk()  
otk.geometry("300x200")   

obtn1 = Button(otk, text = 'click me1')   
obtn2 = Button(otk, text = 'click me2')
obtn3 = Button(otk, text = 'click me3')

# 2. 위젯 배치
obtn1.place(x = 10, y = 60)
obtn2.place(x = 140, y = 60)
obtn3.place(x = 80, y = 10)

otk.mainloop()  

# 배치 매니저 주의 사항!
# pack()과 grid() 혼합 사용 불가능
# grid()와 place() 혼합 가용 불가능