# 과제
# 피자 주문 프로그램


from tkinter import *

tk = Tk()
tk.title("조각피자 주문 프로그램")
tk.geometry("400x300")

price = {
    0: 3200, 
    1: 3500, 
    2: 3600
}

pizza = {
    0: f"치즈 피자 ({price[0]}원)",
    1: f"콤비네이션 피자 ({price[1]}원)",
    2: f"불고기 피자 ({price[2]}원)"
}   

Label(tk, text = "피자").pack()

check_value = {}
for i in range(len(pizza)):
    check_value[i] = BooleanVar()

check_button = {}
for i in range(len(pizza)):
    check_button = Checkbutton(tk, text = pizza[i], variable = check_value[i])
    check_button.pack()
    
result_label = Label(tk, text="", justify="left")
result_label.pack()

def order():
    result = "주문 내역: \n"
    total = 0
    
    for i in range(len(pizza)):
        if check_value[i].get():
            result += f"- {pizza[i]}\n"
            total += price[i]
            
    result += f"\n총 가격: {total}원"
    result_label.config(text = result)
    
button = Button(tk, text = "주문", command = order)
button.pack()

tk.mainloop()
