# bindEvent.py

from tkinter import Tk
from tkinter import Button
from tkinter import Label

# 1. 위젯 생성
otk = Tk()   
otk.geometry("200x350")   

def order():
    print("주문합니다. ")

olabel1 = Label(otk, text = "치즈버거")
olabel2 = Label(otk, text = "불고기버거")
olabel3 = Label(otk, text = "새우버거")
olabel1.pack()
olabel2.pack()
olabel3.pack()

obtn = Button(otk, text = '주문', command = order)   
obtn.pack()


otk.mainloop() 