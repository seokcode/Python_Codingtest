# 양 # B_3184
"""
이 문제는 최단거리 문제는 아니지만 BFS는 꼭 최단거리뿐만 아니라 모든 정점을 1번만 방문
하는 경우에는 다 사용할 수 있으므로 이 문제는 DFS/BFS 둘 다로 풀 수 있다.
"""
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(sx, sy):
    q = deque()
    q.append((sx,sy))
    check[sx][sy] = True
    compare = [0, 0]
    while q:
        x, y = q.popleft()
        if a[x][y] == 'v':  # 늑대면
            compare[0] += 1
        elif a[x][y] == 'o':  # 양이면
            compare[1] += 1

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            # 예외
            # 1. 범위 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 2. 울타리
            if a[nx][ny] == '#':
                continue
            # 3. 이미 방문
            if check[nx][ny]:
                continue
            q.append((nx, ny))
            check[nx][ny] = True
    return compare


n, m = map(int, input().split())
a = [input() for _ in range(n)]
check = [[False]*m for _ in range(n)]  # 방문 체크
d = []
for i in range(n):
    for j in range(m):
        # '#'이 아닌데 방문한 곳이 아니라면 새로운 그룹이므로 bfs를 실시
        if a[i][j] != '#' and not check[i][j]:
            d.append(bfs(i, j))  # 그룹별로 return값 compare변수 푸쉬

v, o = 0,0
for cnt in d:
    if cnt[0] >= cnt[1]:
        v += cnt[0]
    else:
        o += cnt[1]

print(f"{o} {v}")
# == print("o={} v={}" .format(o, v))