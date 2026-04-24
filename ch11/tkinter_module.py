# tkinter_module.py

import tkinter   # 라이브러리 모듈 불러오기

# 1. 위젯 생성
otk = tkinter.Tk()   # 부모 윈도우 위젯 객체 생성

def hello():
    print("hello!")

obtn = tkinter.Button(otk, command = hello)   # 자식 위젯 객체 생성

# 2. 위젯 배치
obtn.pack()   # 위젯 배치

# 3. 이벤트 및 바인딩
# 누름(버튼 이벤트) 발생 시, 특정 동작 수행 (바인딩)

otk.mainloop()   # 주요 반복구조 부모 위젯 실행
