# # 7. 후위 표기법(Postfix Notation, Reverse Polish Notation)으로 
# # 주어진 수식을 계산하는 프로그램을 작성하세요.
# # 후위 표기법에서는 연산자가 피연산자 뒤에 위치합니다. 
# # 예를 들어, 3 4 +는 3 + 4를 의미하며, 결과는 7입니다.
# # 연산자는 +, -, *, /만 고려합니다. (복수 연산자도 처리 가능해야 함.)

# # 후위 표기법 계산기

# def cal(x, y, op):
#     if op == '+':
#         return x + y
#     elif op == '-':
#         return x - y
#     elif op == '*':
#         return x * y
#     elif op == '/':
#         return x / y


# def postfix(expression):
#     stack = []

#     for token in expression.split():

#         # 숫자면 스택에 저장
#         if token.isdigit():
#             stack.append(int(token))

#         # 연산자면 계산
#         else:
#             y = stack.pop()
#             x = stack.pop()

#             result = cal(x, y, token)
#             stack.append(result)

#     return stack.pop()


# # 테스트
# print(postfix("3 4 +"))          # 7
# print(postfix("5 2 * 3 +"))      # 13
# print(postfix("10 2 / 7 +"))     # 12.0
# print(postfix("5 1 2 + 4 * + 3 -"))  # 14


# 8. 리스트를 사용하여 기본적인 큐(queue)를 구현하세요. (다음 내용을 고려할 것.)
# enqueue(x): 정수 x를 큐의 끝에 추가
# dequeue(): 큐의 앞에서 값을 제거하고 반환. 만약 큐가 비어 있다면 -1을 반환
# front(): 큐의 앞에 있는 값을 반환. 만약 큐가 비어 있다면 -1을 반환
# is_empty(): 큐가 비어 있으면 True, 아니면 False를 반환


class Queue:
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self, x):
        self.queue.append(x)
    
    def dequeue(self):
        if self.isempty():
            return -1
        return self.queue.pop(0)
    
    def isempty(self):
        if len(self.queue) == 0:
            return len(self.queue) == 0
    
    def front(self):
        if self.isempty():
          return -1 
        return self.queue[0]
    
    def status_queue(self):
        return self.queue 
        



# 9. 앞서 작성한 큐 클래스를 활용하여 은행에 도착한 고객 순서대로 업무를 처리하는 선입선출(FIFO) 구조의 
# 큐 프로그램을 작성하세요. 리스트를 활용하여 아래 기능을 수행하는 코드를 작성하세요. 
# (다음 조건을 고려할 것.)
# 조건:
# 1. 고객이 도착하면 이름을 큐에 추가합니다 (Enqueue). 
# 2. 업무 처리가 시작되면 가장 먼저 온 고객부터 이름을 출력하고 큐에서 제거합니다 (Dequeue). 
# 3. 현재 대기 중인 고객 명단을 확인하는 기능을 포함하세요.

# 실행 결과 예시)
# 현재 대기열: ['김철수', '이영희', '박민수']   
# 업무 처리 중인 고객: 김철수
# 남은 대기 고객: ['이영희', '박민수']



list = Queue()
list.enqueue("김철수")
list.enqueue("이영희")
list.enqueue("박민수")

print(list.status_queue())
print(list.dequeue())
print(list.status_queue())




# 10. 리스트를 이용하여 덱(deque, 양방향 큐)을 구현하세요. (다음 내용을 고려할 것.)
# push_front(x): 정수 x를 덱의 앞에 추가
# push_back(x): 정수 x를 덱의 뒤에 추가
# pop_front(): 덱의 앞에서 값을 제거하고 반환 (비어 있다면 -1)
# pop_back(): 덱의 뒤에서 값을 제거하고 반환 (비어 있다면 -1)

class Deque:
    def __init__(self):
        self.deque = []
        
    def push_front(self, x):
        self.deque.insert(0, x)
    
    def push_back(self, x):
        self.deque.append(x)
        
    def is_empty(self):
        if len(self.deque) == 0
        return len(self.deque) == 0
    
    def pop_front(self):
        if is_empty():
            return -1
        return self.deque.pop(0)
    
    def pop_back(self)    
        if self.is_empty():
            return -1
        return self.deque.pop()
    
    def status_deque(self):
        return self.deque
    
    