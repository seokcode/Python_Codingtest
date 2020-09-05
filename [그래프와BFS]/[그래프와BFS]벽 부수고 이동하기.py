# 벽 부수고 이동하기 # B_2206
# 벽을 부순적이 없다면 벽/ 빈칸 두가지 선택지가 있지만,
# 벽을 부수고 왔다면 빈칸이라는 한 가지 선택지만 있음
# 즉, (현재, 부순적 없음, 부쉈음)로 상태를 나눠야 함
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
# 상태는 (현재, 부순적 없음, 부쉈음)의 3가지
dist = [[[0]*2 for j in range(m)] for i in range(n)]
q = deque()
q.append((0,0,0))
dist[0][0][0] = 1
while q:
    x,y,z = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            # 갈 수 있는 곳이고 벽은 부순적이 없다면
            if a[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx,ny,z))
            # 벽에 막혀 있고 아직 벽을 부순적이 없다면, 벽을 부수고 난 후에 길이 있다면
            if z == 0 and a[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                q.append((nx,ny,z+1))

# 1. 목표지점에 벽을 부수고 간것과 그냥 간 것 두가지가 모두 존재한다면 그 중 최솟값 출력
if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0:
    print(min(dist[n-1][m-1]))
# 2. 그냥 간 것만 존재함
elif dist[n-1][m-1][0] != 0:
    print(dist[n-1][m-1][0])
# 3. 벽을 부수고 간 것만 존재함
elif dist[n-1][m-1][1] != 0:
    print(dist[n-1][m-1][1])
else:
    print(-1)