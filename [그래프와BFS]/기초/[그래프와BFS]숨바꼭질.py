# 숨바꼭질 # B_1697
# 동생을 찾는 가장빠른시간을 구하는 문제(BFS)
from collections import deque
MAX = 200000
check = [False]*(MAX+1)
dist = [-1]*(MAX+1)
n, m = map(int, input().split())
check[n] = True
dist[n] = 0  # 걸리는 시간 계산
q = deque()
q.append(n)

while q:
    now = q.popleft()
    for nxt in [now-1, now+1, now*2]:
        if 0 <= nxt <= MAX and check[nxt] == False:
            check[nxt] = True  # 방문했음을 표시
            dist[nxt] = dist[now] + 1  # 걸리는 시간 계산
            q.append(nxt)

print(dist[m])
