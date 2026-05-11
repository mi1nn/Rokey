# stack.class.py

class Stack:
    # 1. 멤버 변수
    def __init__(self):
        self.stack = []
        
    # 2. push
    # 기능: 스택에 데이터 넣기 
    # 입력: 데이터
    # 출력: 없음
    def push(self, data):
        self.stack.append(data)
        
    # 3. pop
    # 기능: 스택에서 데이터 제거하기
    # 입력: 없음
    # 출력: 스택 내 상단 데이터
    def pop(self):
        # 스택이 비어있는 경우 고려
        if not self.is_empty():
            return self.stack.pop()
        return
    
    # 4. 스택 내 데이터 유무 확인
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    # 5. 스택 최상위(Top) 데이터 확인
    def peak(self):
        # 스택이 비어있는 경우 고려
        if not self.is_empty():
            return self.stack[-1]

    # 6. 스택 상태 변환
    def status_stack(self):
        return self.stack



if __name__ == "__main__":
    my_stack = Stack()
    print(my_stack.peak())
    my_stack.pop()
    my_stack.push(7)
    my_stack.push(2)
    my_stack.pop()
    print(my_stack.status_stack())
    my_stack.push(3)
    my_stack.push(6)
    print(my_stack.peak())
    print(my_stack.status_stack())