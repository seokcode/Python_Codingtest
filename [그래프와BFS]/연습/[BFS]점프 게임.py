# 점프 게임 # B_15558
"""
# BFS는 할수 있다/없다의 문제 또한 최단거리가 존재한다/존재하지않는다로 구할 수 있음
# i번칸을 방문한 초가 i초보다 크면 방문 못하는 것
"""
from collections import deque

n, k = map(int,input().split())
a = [input() for _ in range(2)]
dirs =[(0,1),(0,-1),(1,k)]
cnt = [[-1]*n for _ in range(2)]
q = deque()
q.append((0,0))
cnt[0][0] = 0
ok = False
# 목적지는 (1,n)

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = (x+dx)%2, y+dy  # (x+dx)%2 = 0혹은 1만 나옴
        if ny >= n:  # 답인 경우
            ok = True
            break
        if ny < 0:  # 갈 수 없는 경우
            continue
        if cnt[nx][ny] != -1:  # 한번 간 칸을 또 가는건 최단거리가 아님
            continue
        if a[nx][ny] == '0':  # 갈 수 없는 곳
            continue
        if ny < cnt[x][y] + 1:
            # 밟을 칸의 번호가 곧 그 칸이 물에잠기는 초를 의미하므로
            # 밟을 칸의 번호가 현재까지 걸린 시간 + 1 보다 작다면 못감.
            continue
        cnt[nx][ny] = cnt[x][y] + 1
        q.append((nx,ny))
    if ok:
        break

print(1 if ok else 0)