# 연구소 # B_14502
"""
# BFS+브루트포스 / 그냥 BFS 알고리즘에도 있음
# 전체 탐색에 소요: NM, 벽 세개 세워야 함: NM^3
# 총 시간 복잡도: O(NM^4) => 16,777,216
# 개인적으로는 벽을 세우는 부분은 재귀 함수로 구현하는게 훨씬 간단 -> [BFS]연구소.py 참조
"""

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
            if b[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
                b[nx][ny] = 2
                q.append((nx,ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt
# ------여기까진 BFS------- #

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0

# 벽 3개 세우기 벽 하나 당 2중포문 한 쌍 => 6중 포문
for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0:  # 벽 1
            continue
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0:  # 벽 2
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] != 0:  # 벽 3
                            continue

                        # 벽1,2,3이 세워질 위치가 같지 않기 위해 확인
                        # 같으면 다시 찾기 위해 넘김
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue

                        # 벽 세우기
                        a[x1][y1] = 1
                        a[x2][y2] = 1
                        a[x3][y3] = 1

                        cur = bfs(a)
                        if ans < cur:
                            ans = cur  # 최댓값 구하기

                        # 한 턴 끝났으니 다른 케이스를 위해 초기화
                        a[x1][y1] = 0
                        a[x2][y2] = 0
                        a[x3][y3] = 0
# -----브루트포스----- #

print(ans)
