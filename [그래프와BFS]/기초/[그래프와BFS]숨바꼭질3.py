# 숨바꼭질3 # B_13549
# BFS로 최적경로를 찾을 수 있는 조건 중 하나인 모든 가중치가 동일함에 어긋남
# 왜? 순간이동의 가중치가 0임
# 방법1. BFS를 큐를 두개(0초걸리는거/1초걸리는거) 사용하여 해결
# 방법2. 덱을 사용 가중치가 1은 우측에 0은 좌측에 추가하여 해결

# [방법 2]
from collections import deque
MAX = 200000
check = [False]*MAX
dist = [-1]*MAX
n,m = map(int, input().split())
check[n] = True
dist[n] = 0
q = deque()
q.append(n)
while q:
    now = q.popleft()
    if now*2 < MAX and check[now*2] == False:
        q.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]
    if now-1 >= 0 and check[now-1] == False:
        q.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now]+1
    if now+1 < MAX and check[now+1] == False:
        q.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now]+1

print(dist[m])

"""
[방법 1]
from collections import deque
MAX = 200000 
check = [False]*MAX
dist = [-1]*MAX
n,m = map(int,input().split())
check[n] = True
dist[n] = 0
q = deque()
next_queue = deque()
q.append(n)
while q:
    now = q.popleft()
    if now*2 < MAX and check[now*2] == False:
        q.append(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]
    if now-1 >= 0 and check[now-1] == False:
        next_queue.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now]+1
    if now+1 < MAX and check[now+1] == False:
        next_queue.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now]+1
    if not q:
        q = next_queue
        next_queue = deque()

print(dist[m])
"""