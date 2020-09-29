# 알고스팟 # B_1261
# 이 문제에서의 가중치는 (벽을 부순 것: 1 / 안 부순 것: 0)
# 즉, 가중치가 동일하지 않기 떄문에 큐를 두개 사용하거나 덱을 하나 사용
# 왜? 문제의 해답이 도착점까지의 최적 경로가 아닌 벽을 부순 최솟값이기 때문
from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]
m, n = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
q = deque()
q.append((0, 0))
dist[0][0] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                if a[nx][ny] == 0:
                    q.appendleft((nx, ny))
                    dist[nx][ny] = dist[x][y]
                else:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1

print(dist[n-1][m-1])