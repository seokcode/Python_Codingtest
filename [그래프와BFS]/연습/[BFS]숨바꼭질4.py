# 숨바꼭질4 # B_13913
# 이동경로도 출력해야 함
from collections import deque
import sys

MAX = 200000
sys.setrecursionlimit(MAX)
check = [False]*MAX
dist = [-1]*MAX
via = [-1]*MAX

n, k = map(int,input().split())
check[n] = True
dist[n] = 0  # 걸리는 시간 계산
q = deque()
q.append(n)

while q:
    now = q.popleft()
    if now - 1 >= 0 and not check[now - 1]:
        q.append(now - 1)
        check[now - 1] = True
        dist[now - 1] = dist[now] + 1
        via[now - 1] = now
    if now + 1 < MAX and not check[now + 1]:
        q.append(now + 1)
        check[now + 1] = True
        dist[now + 1] = dist[now] + 1
        via[now + 1] = now
    if now * 2 < MAX and not check[now * 2]:
        q.append(now * 2)
        check[now * 2] = True
        dist[now * 2] = dist[now] + 1
        via[now * 2] = now


def path(n, k):
    if n != k:
        path(n, via[k])
    print(k, end=' ')

print(dist[k])
path(n, k)
