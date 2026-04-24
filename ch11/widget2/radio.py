# radio.py

# bindEvent.py

from tkinter import Tk
from tkinter import Button
from tkinter import Radiobutton
from tkinter import IntVar

# 1. 위젯 생성
otk = Tk()   
otk.geometry("200x350")   

radio_value = IntVar()   # 정수형 변수 저장객체 생성
radio_value.set(2)
# radio_value.set(2)   # 정수값 설정
# val = radio_value.get()   # 정수값 접근
# print(val)

lunch = {0: "A 런치", 1: "B 런치", 2: "C 런치"}

# radio_value -> 어떤 버튼이 선택되어 있는지 저장할 변수
# variable -> 클릭된 버튼의 정보를 저장할 변수명 설정
# value -> radio_value에 저장할 데이터를 지정하는 변수
orb1 = Radiobutton(otk, text = lunch[0], variable = radio_value, value = 0)
orb2 = Radiobutton(otk, text = lunch[1], variable = radio_value, value = 1)
orb3 = Radiobutton(otk, text = lunch[2], variable = radio_value, value = 2)

# 기능: 선택된 체크버튼의 값을 변수로 가져와 출력
def buy():
    print("다음 메뉴를 주문합니다. ")
    val = radio_value.get()
    print(lunch[val])

obtn1 = Button(otk, text = "주문", command = buy)

# 2. 위젯 배치
orb1.pack()
orb2.pack()
orb3.pack()
obtn1.pack()

otk.mainloop()

 
# class IntVar:
#     def __init__(self):
#         self.int_val = 0
        
#     def ser(self, int_val):
#         self.int_val = int_val
        
#     def get(self):
#         return self.int_val