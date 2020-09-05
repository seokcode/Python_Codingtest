# 레이저 통신  # B_6087
"""
레이저는 한 방향으로 끝까지 뻗음 == 직선으로 생각
거울은 각각 들어오는 레이저와, 반사되어 나가는 레이저 2개를 담당
따라서 레이저로 뻗는 총 직선 수 -1 이 거울의 갯수
"""
from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]

w, h = map(int, input().split())
a = [list(input()) for _ in range(h)]

start_x = start_y = end_x = end_y = -1
# point[0][0],[0][1] : start
for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            if start_x == -1:
                start_x, start_y = i, j
            else:
                end_x, end_y = i, j

d = [[-1]*w for _ in range(h)]
q = deque()
q.append((start_x, start_y))
d[start_x][start_y] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        while 0 <= nx < h and 0 <= ny < w:
            if a[nx][ny] == '*':
                break
            if d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
            nx += dx[k]
            ny += dy[k]

# 항상 거울 갯수는 직선 갯수보다 한개 적음
# 거울 당 직선 두개를 담당하기 때문
print(d[end_x][end_y]-1)
