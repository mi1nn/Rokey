# raise1.py

# raise 예외클래스명(에외정보데이터):
# print("raise")

# 예외 발생시키기
# raise NameError("Hi There")   # 프로그램 중단

# try:
#     raise NameError("Hi There")
# except NameError as e:
#     print("An exception flew by")
#     print("e: ", e)

# print("exit")

# 사용 예
# 잘못된 값 들어왔을 때 방지
# 함수에서 조건을 위반 시 실행 중단
# 사용자 정의 에러 처리

# 예) 은행 잔고 부족 시 예외 발생
class InsufficientBalanceError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, account):
        if account > self.balance:
            raise IndentationError("잔고가 부족합니다. ")
        self.balance -= account
        return self.balance

# raise InsufficientBalanceError("잔고가 부족합니다. ")

lim = Account(1000)
lim.withdraw(2000)