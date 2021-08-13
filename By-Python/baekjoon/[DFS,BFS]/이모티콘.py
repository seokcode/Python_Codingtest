# 이모티콘 # B_14226
import sys
from collections import deque
n = int(sys.stdin.readline())
# n=2라면 0,1,2필요하니까 n+1
dist = [[-1]*(n+1) for _ in range(n+1)]
q = deque()
q.append((1, 0))
dist[1][0] = 0  # 이모티콘이 1개 있는 상태로 시작
while q:
    s, c = q.popleft()
    # 1. c(clipboard)에 복사 / (s,c->s)
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        q.append((s, s))
    # 2. 붙여넣기 / 화면에 있는 s개 +클립보드에 있던거 c (s+c, c)
    if s+c <= n and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    # 3. 화면에 있는거 1개 삭제 / (s-1,c)
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))

ans = -1  # 최솟값을 가리기위한 설정값
for i in range(n+1):
    if dist[n][i] != -1:
        if ans == -1 or ans > dist[n][i]:
            ans = dist[n][i]

print(ans)
