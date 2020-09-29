# 유기농 배추 # B_1012
# 단지번호 붙이기와 유사문제

from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]
t = int(input())  # test_case

def bfs(x, y, cnt):
    q = deque()
    # 현 위치 큐에 push
    q.append((x,y))
    group[x][y] = cnt
    # 큐에 값이 있는 동안 반복
    while q:
        # 현 위치 큐에서 pop
        x, y = q.popleft()
        for k in range(4):
            # 자신의 위치 기준 상하좌우로 배추가 있는지 있다면 방문했던 곳인지 검사
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    # 배추가 있고 방문하지 않았었다면
                    # q에 해당 위치 push(해당 위치로부터 상하좌우 검사)
                    q.append((nx, ny))
                    # 해당 위치에 현재 cnt(그룹번호) 부여
                    group[nx][ny] = cnt


for _ in range(t):
    m, n, k = map(int, input().split())
    a = [[0]*m for _ in range(n)]  # 배추 있는 곳 입력
    group = [[0]*m for _ in range(n)]  # 방문&그룹 표시
    q = deque()

    # 배추 있는 곳 입력
    for _ in range(k):
        j, i = map(int, input().split())
        a[i][j] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            # 배추가 있는데 방문한 곳이 아니라면 새로운 그룹
            if a[i][j] == 1 and group[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)

    print(cnt)
