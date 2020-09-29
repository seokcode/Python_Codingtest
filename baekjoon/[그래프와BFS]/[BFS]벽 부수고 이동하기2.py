# 벽 부수고 이동하기2 # B_14442
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n, m, cnt = map(int,input().split())
a = [list(map(int,input())) for _ in range(n)]
dist = [[[0]*11 for j in range(m)] for i in range(n)]  # *11? : 1<=k<=10이기 때문
q = deque()
q.append((0,0,0))
dist[0][0][0] = 1

while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            # 갈 수 있는 곳이고 벽은 부순적이 없다면
            if a[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))
            # 벽에 막혀 있고 아직 벽을 부순적이 없다면, 벽을 부수고 난 후에 길이 있다면
            # 벽 부순 횟수가 부술 수 있는 횟수 이하라면
            if z+1 <= cnt and a[nx][ny] == 1 and dist[nx][ny][z + 1] == 0:
                dist[nx][ny][z + 1] = dist[x][y][z] + 1
                q.append((nx, ny, z + 1))

ans = -1
# 최솟값 도출
for i in range(cnt+1):
    if dist[n-1][m-1][i] > 0:
        if ans == -1 or ans > dist[n-1][m-1][i]:
            ans = dist[n-1][m-1][i]
print(ans)
