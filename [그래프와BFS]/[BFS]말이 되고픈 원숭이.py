# 말이 되고픈 원숭이 # B_1600
from collections import deque
# 4방향, 나이트의 이동 방식
dx = [0,0,1,-1, -2,-1,1,2,2,1,-1,-2]
dy = [1,-1,0,0, 1,2,2,1,-1,-2,-2,-1]
cost = [0,0,0,0, 1,1,1,1,1,1,1,1]

l = int(input())  # 나이트처럼 이동할 수 있는 횟수
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[[-1]*31 for j in range(m)] for i in range(n)]  # 나이트처럼 이동할 수 있는 최대 횟수 0<=k<=30
q = deque()
q.append((0, 0, 0))
d[0][0][0] = 0

while q:
    x, y, c = q.popleft()
    for k in range(12):
        # 이번 nx,ny,nc 에서 12개의 방향을 다 가봄 >> 방문 체크하며 반복
        nx, ny, nc = x+dx[k], y+dy[k], c+cost[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1:  # 장애물
                continue
            if nc <= l:  # 나이트처럼 이동할 수 있는 횟수가 남았다면
                if d[nx][ny][nc] == -1:
                    d[nx][ny][nc] = d[x][y][c] + 1
                    q.append((nx, ny, nc))

ans = -1
for i in range(l+1):
    if d[n-1][m-1][i] > -1:
        if ans == -1 or ans > d[n-1][m-1][i]:
            ans = d[n-1][m-1][i]

print(ans)
