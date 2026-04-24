# checkbutton.py

from tkinter import Tk
from tkinter import Button
from tkinter import BooleanVar
from tkinter import Checkbutton

# 1. 위젯 생성
otk = Tk()   
otk.geometry("200x350")

coffee = {0: "아메리카노", 
          1: "라떼", 
          2: "카푸치노", 
          3: "에스프레소"}

check_value = {}   # check_value가 리스트라면, for문에 append를 사용해야함
for i in range(len(coffee)):
    check_value[i] = BooleanVar()

# check_value1 = BooleanVar()    
# check_value2 = BooleanVar()
# check_value3 = BooleanVar()
# check_value4 = BooleanVar()

# check_value1.set(True)
# val1 = check_value1.get()

for i in range(len(coffee)):
    ocheckButton = Checkbutton(otk, text = coffee[i], variable = check_value[i])
    ocheckButton.pack()

# ocheckButton1 = Checkbutton(otk, text = coffee[0], variable = check_value[0])
# ocheckButton2 = Checkbutton(otk, text = coffee[1], variable = check_value[1])
# ocheckButton3 = Checkbutton(otk, text = coffee[2], variable = check_value[2])
# ocheckButton4 = Checkbutton(otk, text = coffee[3], variable = check_value[3])

# 기능: 선택된 체크버튼의 값을 변수로 가져와 출력
def buy():
    print("다음 메뉴를 주문합니다. ")
    for i in range(len(coffee)):
        if check_value[i].get():
            print(coffee[i])
            


obtn1 = Button(otk, text = "주문", command = buy)

# ocheckButton1.pack()
# ocheckButton2.pack()
# ocheckButton3.pack()
# ocheckButton4.pack()
obtn1.pack()

otk.mainloop()
