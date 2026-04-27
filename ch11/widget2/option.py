# option.py

from tkinter import Tk
from tkinter import StringVar
from tkinter import OptionMenu

# 1. 위젯 생성
otk = Tk()
otk.geometry("400x300")

option_list = ['Optional1', 'Optional2', 'Optional3']

selected_option = StringVar()

selected_option.set(option_list[0])
# sel_option = selected_option.get()
# print(sel_option)

# option_menu = OptionMenu(otk, selected_option, option_list[0], option_list[1], option_list[2])
# * 역할: 컨테이너 자료 -> 개별 인자로 분해 (언패킹)
option_menu = OptionMenu(otk, selected_option, *option_list)

option_menu.pack()

sel_option = selected_option.get()
print(sel_option)

otk.mainloop()