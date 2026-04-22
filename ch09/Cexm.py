# Cexm.py

class Cexm:
    def fsam(self):
        print("멤버 함수(메서드)")
    def fsbm(self, pa):
        self.x = pa
        print("멤버 변수 x: ", self.x)

ca = Cexm()   # 인스턴스 객체 생성
ca.fsam()   # 메서드 호출
ca.fsbm(10)   # 메서드 호출

cb = Cexm()   # 인스턴스 객체 생성
cb.fsam()
cb.fsbm(20)
print(cb.x)

# print(id(Cexm()))
# print(id(ca))
# print(id(cb))

