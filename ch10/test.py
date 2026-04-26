# 과제 

class Phone:
    def __init__(self, number, color):
        self.number = number
        self.color = color

phone = Phone("010-1234-1234", "검정")
print(phone.number)
print(phone.color)