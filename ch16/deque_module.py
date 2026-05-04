# deque_module.py

from collections import deque

dq = deque()
print(type(dq))

dq.append(1)  # 뒤로 삽입
dq.appendleft(2)   # 앞으로 삽입
print(dq)

dq.pop()   # 마지막 데이터 제거
dq.popleft()   # 처음 데이터 제거
print(dq)
