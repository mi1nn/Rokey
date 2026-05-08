# dfs.py

# # 탐색할 노드를 담을 스택 자료형 생성
# stack = list()   # stack = []

# # 각 노드가 방문한 노드인지를 구분할 수 있는 리스트 생성
# visited = list()

# # 탐색 시작 노드(첫번째 노드)를 스택에 삽입
# stack.append(1)

# 6. 4~5번 반복
# while stack:
#     # 방문할 노드를 스택에서 하나씩 꺼내기
#     node = stack.pop()
# # 스택에서 꺼낸 노드가 방문한 노드가 아니면, 그 인접 노드를 스택에 삽입하고 방문 처리
#     if node not in visited:
#         # 인접 노드를 스택에 추가
#         # stack.append(graph[node])
#         # stack.extend(graph[node])
#         stack.extend(reversed(graph[node]))
#         visited.append(node)
        

# 매개변수: 그래프
# 반환값: 방문 기록

myGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F'],
}

start_node = 'A'

def my_dfs(graph, start_node):
    
    # 1. 탐색할 노드를 담을 스택
    stack = list()
    
    # 2. 빙문 여부 확인 리스트
    visited = list()

    # 3. 탐색 시작 노드
    stack.append(start_node)
    
    # 6. 4~5번 반복
    while stack:
        # 4. 방문할 노드를 스택에서 제거
        node = stack.pop()
        # 5. 스택에서 꺼낸 노드가 방문한 노드가 아니면, 그 인접 노드를 스택에 삽입하고 방문 처리
        if node not in visited:
            # 인접 노드를 스택에 추가
            # stack.append(graph[node])
            # stack.extend(graph[node])
            stack.extend(reversed(graph[node]))
            visited.append(node)  # 방문 처리
            print(f"visited: {visited}")
            print(f"stack: {stack}")
            print()

    return visited

print(my_dfs(myGraph, 'A'))

from graph1 import graph1
print(my_dfs(graph1, 3))