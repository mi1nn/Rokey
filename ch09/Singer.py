# Singer.py

# 클래스: 객체들
# 가수: 아이유, BTS
# 속성(데이터, 명사): 변수 -> 이름
# 기능(동작, 동사): 함수 -> 노래부르다

class Singer:
    # name = "IU
    job = "가수"
    def call_name(self, name):
        self.name = name
    def sing(self):
        print("이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요. ")


print(Singer.job)
IU = Singer()  # 생성자 함수
# print(IU.name)  # 속성 확인
# IU.sing()  # 기능 확인

bts = Singer()
# print(bts.name)

print(IU.job)
IU.call_name("IU")
print(IU.name)
IU.sing()

print(bts.job)
bts.call_name("BTS")
print(bts.name)