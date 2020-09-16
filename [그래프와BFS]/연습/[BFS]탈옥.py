# 탈옥 # B_9238
"""
교안참조(연습)
밖 아무곳->모든공간, 죄수1->밖, 죄수2->밖 이상 세가지를 출발점으로 하여 BFS
BFS를 하는데에 NM의 시간이 걸리고 이걸 총 세 번 하기때문에 O(NM)
"""

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a, x, y):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((x,y))
    dist[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and a[nx][ny] != '*':
                if a[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx,ny))
    return dist

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = ['.'+input()+'.' for _ in range(n)]
    n += 2
    m += 2
    a = ['.'*m] + a + ['.'*m]
    d0 = bfs(a, 0, 0)
    x1=y1=x2=y2=-1
    for i in range(n):
        for j in range(m):
            if a[i][j] == '$':
                if x1 == -1:
                    x1,y1 = i,j
                else:
                    x2,y2 = i,j
    d1 = bfs(a,x1,y1)
    d2 = bfs(a,x2,y2)
    ans = n*m

    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                continue
            # 세 방향에서 구한 BFS의 값을 다 더함
            cur = d0[i][j] + d1[i][j] + d2[i][j]

            if a[i][j] == '#':
                # 3가지 방법이 모이는 칸이 문이라면 문은 한번만 열면 되므로
                # 총 3가지의 BFS로 인한 중복된 횟수가 나오므로 2가지는 빼줘야함
                cur -= 2
            ans = min(ans,cur)
    print(ans)

