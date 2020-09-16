# 섬의 개수 # B_4963
# 플러드 필에서 갈 수 있는 방향에 대각선 추가하면 같은 문

import sys
from collections import deque
from functools import reduce
# dx:행, dy:열
# 갈 수 있는 방향을 나타냄
# 오른, 왼, 아래, 위, 왼위대각, 왼아대각, 오위대각, 오아대각
dx = [0,0,1,-1,-1,1,-1,1]
dy = [1,-1,0,0,-1,-1,1,1]


def bfs(x, y, cnt):
    q = deque()
    # 현 위치 큐에 push
    q.append((x,y))
    group[x][y] = cnt
    # 큐에 값이 있는 동안 반복
    while q:
        # 현 위치 큐에서 pop
        x, y = q.popleft()
        for k in range(8):
            # 자신의 위치 기준 상하좌우로 집이 있는지 있다면 방문했던 곳인지 검사
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    # 집이 있고 방문하지 않았었다면
                    # q에 해당 위치 push(해당 위치로부터 상하좌우 검사)
                    q.append((nx, ny))
                    # 해당 위치에 현재 cnt(그룹번호) 부여
                    group[nx][ny] = cnt


while True:
    # m: 행  n: 열
    m, n = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    a = [list(map(int, list(input().split()))) for _ in range(n)]
    group = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and group[i][j] == 0:
                # cnt 값이 +1 된다는 것은 한 그룹의 탐색이 종료되었음을 의미
                cnt += 1
                bfs(i, j, cnt)

    print(cnt)
