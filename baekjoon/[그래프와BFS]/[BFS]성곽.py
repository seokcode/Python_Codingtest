# 성곽 # B_2234
"""
하나의 벽을 제거해서 얻을 수 있는 가장 넓은 방의 크기?
BFS 한번 할 때 O(NM)인데 하나씩 다 제거해보려면 O(NM^2) -> 너무 오래걸림
그래서 다른 방법을 사용
"""
from collections import deque
dx = [0,-1,0,1]
dy = [-1,0,1,0]

m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*m for _ in range(n)]


def bfs(x, y, rooms):
    q = deque()
    q.append((x,y))
    d[x][y] = rooms
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] != 0:
                continue
            if (a[x][y] & (1<<k)) > 0:
                continue
            q.append((nx, ny))
            d[nx][ny] = rooms
    return cnt


rooms = 0
room = [0]
for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            rooms += 1
            room.append((bfs(i, j, rooms)))
print(rooms)  # 1.이 성에 있는 방(그룹)의 갯수

ans = 0
for i in range(1, rooms+1):
    if ans < room[i]:
        ans = room[i]
print(ans)  # 2.가장 넓은 방의 넓이

ans = 0
for i in range(n):
    for j in range(m):
        x, y = i, j
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] == d[x][y]:  # 방번호가 같으면 건너 뜀
                continue
            if (a[x][y] & (1<<k)) > 0:
                if ans < room[d[x][y]]+room[d[nx][ny]]:
                    ans = room[d[x][y]]+room[d[nx][ny]]
print(ans)  # 3.하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기

