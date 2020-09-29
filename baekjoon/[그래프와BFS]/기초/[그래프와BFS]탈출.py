# 탈출 # B_3055
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
r, c = map(int, input().split())  # r:행 c:열
a = [list(list(input())) for _ in range(r)]
water = [[-1]*c for _ in range(r)]
dist = [[-1]*c for _ in range(r)]
q = deque()
for i in range(r):
    for j in range(c):
        if a[i][j] == '*':  # *:물
            q.append((i, j))
            water[i][j] = 0
        elif a[i][j] == 'S':  # 출발점
            sx, sy = i, j
        elif a[i][j] == 'D':  # 도착점
            ex, ey = i, j
# 물이 퍼지는 시간을 먼저 계산
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if water[nx][ny] != -1:
                continue
            if a[nx][ny] in 'XD':
                continue
            water[nx][ny] = water[x][y] + 1
            q.append((nx,ny))

# 큐가 비어있는 상태, 시작을 위해 고슴도치의 출발점 입력
q.append((sx,sy))
dist[sx][sy] = 0
# 물이 퍼지는 시간과 고슴도치의 이동 시간을 비교하며 물에 닿지 않고 도착할 수 있는지 파악
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if dist[nx][ny] != -1:
                continue
            if a[nx][ny] in 'X':
                continue
            if water[nx][ny] != -1 and dist[x][y] + 1 >= water[nx][ny]:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))

if dist[ex][ey] == -1:
    print('KAKTUS')
else:
    print(dist[ex][ey])