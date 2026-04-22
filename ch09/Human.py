# Human.py

class Human:
    
    eyes = 2
    nose = 1
    mouth = 1
    
    def __init__(self, age, name):
    # 인스턴스 변수
        self.age = age
        self.name = name

    # 기능: 자기소개
    def info(self):
        print(str(self.age) + "살:", end = " ")
        print(str(self.name))

# 추가 기능 구현
# 먹다, 자다, 말하다 를 출력하는 기능
    
    def sleep(self):
        print("자다")
        
    def talk(self):
        print("말하다")
        
    def eat(self, food):
        self.food = food
        print(self.food + "먹다")
        
print("눈 개수: ", Human.eyes)
print("코 개수: ", Human.nose)
print("입 개수: ", Human.mouth)

kim = Human(27, "김기기")
kim.info()
kim.eat("라면")

lee = Human(32, "이두두")
lee.info()


