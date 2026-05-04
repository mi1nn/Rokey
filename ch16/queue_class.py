# queue_class.py

class Queue:
    
    # 데이터 공간 초기화
    def __init__(self):
        self.queue = []
    
    # 1. Enqueue
    def enqueue(self, data):
        self.queue.append(data)
    
    # 2. Dequeue
    def dequeue(self):
        # 큐가 비어있는 경우 고려
        if not self.is_empy():
            return self.queue.pop(0)
        return
    
    # 3. 큐가 비어있는 경우
    def is_empy(self):
        if len(self.queue) == 0:
            return True
        return False
    
    # 4. 큐 상태 변환
    def status_queue(self):
        return self.queue
    
if __name__ == "__main__":
    q1 = Queue()   # 큐 생성
    q1.dequeue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.dequeue()
    print(q1.status_queue())
    q1.enqueue(4)
    q1.dequeue()
    q1.enqueue(5)
    print(q1.status_queue())