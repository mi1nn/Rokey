# p1.py

# 문제1. 은행 번호표 시스템
# 은행에서 고객 상담을 위해 번호표 대기 시스템을
# 만들려고 합니다. 앞서 학습한 2 자료구조 중 선택해 작성
# Queue
# 1: 철수, 2: 영희, 3: 민수

from queue_class import Queue
bank = Queue()
bank.enqueue("철수")
bank.enqueue("영희")
bank.enqueue("민수")
print(bank.status_queue())
print(bank.dequeue())   # 첫번째 상담자
print(bank.status_queue())

# 문제 2. 브라우저 뒤로가기 시스템
# 웹 브라우저 방문 기록을 관리하는 프로그램 작성
# 앞서 학습한 2 자료구조 중 선택해 작성
# Stack

from stack_class import Stack
browser = Stack()
browser.push("네이버")
browser.push("구글")
browser.push("유튜브")
print(browser.status_stack())
print(browser.pop())   # 뒤로가기 버튼 클릭
print(browser.peak())  # 현재 위치한 사이트
print(browser.status_stack())


# Deque
# 브라우저: 앞 / 뒤 이동
# 문서편집기: Undo / Redo
