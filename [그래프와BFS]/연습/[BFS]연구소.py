# 연구소 # B_14502
from collections import deque

def bfs():
    global final
    result = 0
    copy = [[-1]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            copy[i][j] = a[i][j]

    # bfs가 진행 될 때 마다 초기 q에는 항상 2의 위치가 있어야 함
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if copy[nx][ny] == 0:
                    copy[nx][ny] = 2
                    q.appendleft((nx, ny))


    for i in range(n):
        for j in range(m):
            if copy[i][j] == 0:
                result += 1

    final = max(final, result)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                a[i][j] = 1
                wall(cnt+1)
                a[i][j] = 0


n, m = map(int, input().split())
a = [list(map(int, list(input().split()))) for _ in range(n)]
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
final = 0


wall(0)
print(final)