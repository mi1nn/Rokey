# Pizza_class.py

# class 클래스명:
#     1. 멤버변수
#     변수명 = 속성값
#     2. 멤버함수 (메서드)
#     def 함수명(self, 매개변수):  # 클래스 내의 함수 매개변수 앞에 self 작성
#         함수 내부 멤버변수 작성할 경우
#         self.멤버변수 = 속성값
#         코드블럭
#         return 반환값

# 빈 클래스 
# class 클래스명:
#     pass  # -> 아직 뭘 작성할지 몰라서 일단 넘어가라 / 안적으면 문법오류


# 클래스 정의
class Pizzaclass:
    # name = "Papajohns"
    def order(self):
        print("주문하다. ")
        self.kind = 10

# 객체 생성 (클래스 사용)
na = Pizzaclass() # (객체) 생성자 함수

# print(na.name)
na.order()  # 객체.메서드()
print(na.kind)  # 객체.멤버변수
