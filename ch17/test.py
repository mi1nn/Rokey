maze = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
]

for row in maze:
    print(row)
    
# 8. 앞서 작성한 리스트에서 1차원 데이터의 길이는 지도의 가로 크기를 2차원 
# 데이터의 길이는 지도의 세로 크기를 표현한다. 세로(행)과 가로(열) 두 수와 길과 벽을 
# 표현하기 위한 데이터를 입력 받아 앞서 제시한 지도를 표현한 리스트를 작성하시오.

# row = int(input("세로 크기 입력: "))
# col = int(input("가로 크기 입력: "))

# maze = []

# print("지도 데이터 입력 (0: 길, 1: 벽)")

# for i in range(row):
#     line = list(map(int, input().split()))
#     maze.append(line)

# print("생성된 지도:")
# for m in maze:
#     print(m)
    


visited = [[False] * 6 for _ in range(6)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    if x < 0 or x >= 6 or y < 0 or y >= 6:
        return

    if maze[x][y] == 1 or visited[x][y]:
        return

    visited[x][y] = True

    print(f"({x}, {y}) 방문")

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        dfs(nx, ny)

dfs(0, 0)