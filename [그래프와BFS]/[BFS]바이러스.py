# 바이러스 # B_2606
from collections import deque

com = int(input())
n = int(input())
matrix = [[0] * (com + 1) for _ in range(com + 1)]
visited = [[False] * (com + 1) for _ in range(com + 1)]
q = deque()
for _ in range(n):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1


q.append(1)
def bfs(matrix):
    ans = [1]
    while q:
        x = q.popleft()

        for j in range(1, com + 1):
            if matrix[x][j] == 1 and not visited[x][j]:
                q.appendleft(j)
                visited[x][j] = True
                visited[j][x] = True
                if not j in ans:  # 중복되는 컴퓨터 번호 방지
                    ans.append(j)
    return len(ans)-1


print(bfs(matrix))
