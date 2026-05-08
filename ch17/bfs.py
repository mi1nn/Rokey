# bfs.py

from graph import myGraph

def my_bfs(graph, start_node):
    queue = list()   # 1. 방문할 노드를 담을 큐 자료형 생성
    visited = list()   # 2. 각 노드가 방문한 노드인지를 구분할 수 있는 리스트 생성
    queue.append(start_node)   # 3. 탐색 시작 노드(첫번째 노드)를 큐에 삽입

    # 6. 더이상 방문할 노드가 없을 때까지 반복
    while queue:   # queue에 내용이 남아있으면 반복
        node = queue.pop(0)   # 4.방문할 노드를 큐에서 하나씩 꺼내시

        if node not in visited:   # 5. 큐에서 꺼낸 노드가 방문한 노드가 아니면
            queue.extend(graph[node])   # 그 인접 노드를 큐에 삽입하고
            visited.append(node)   # 방문 처리
            print(f"queue: {queue}")
            print(f"visited: {visited}")
            print()
    
    return visited

print(my_bfs(myGraph, 'A'))

from graph1 import graph1
print(my_bfs(graph1, 3))