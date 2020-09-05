# 토마토 # B_7576

import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
m, n = map(int, sys.stdin.readline().split())
a = [list(map(int, list(input().split()))) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
# a 리스트에 -1(토마토가 없는 곳)이 표시되어 있기 때문에 a=0/ dist=-1인곳을
# 탐색하면 됨. 따라서 dist에는 토마토가 없는 곳을 표시할 필요 없음
cnt = 0
q = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            dist[i][j] = 0
            q.append((i,j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

# dist= [[0, -1, 6, 5, 4, 3], [1, -1, 5, 4, 3, 2], [2, 3, 4, 5, -1, 1], [3, 4, 5, 6, -1, 0]]
# [max(row) for row in dist] = [6, 5, 5, 6]
# max([max(row) for row in dist]) = 6
ans = max([max(row) for row in dist])
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and dist[i][j] == -1:
            ans = -1

print(ans)
