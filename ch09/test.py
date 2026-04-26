# 과제 내용 테스트

# 9. 핸드폰 (Phone) 클래스에 (제조사, 출고년도, 색상)을 매개변수로 사용하여 기 생성된 맴버 변수를 수정하는 setInfo 메소드를 추가하세요.

class Phone:
    def __init__(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color
        
    def info(self):
        print("제조사:", self.company)
        print("출고년도:", self.year)
        print("색상:", self.color)




my_phone = Phone()