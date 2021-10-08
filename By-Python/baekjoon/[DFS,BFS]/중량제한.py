from collections import deque

def bfs(start, end, mid):
  visited[start] = True
  q = deque()
  q.append(start)

  while q:
    now = q.popleft()

    if now == end:
      return True

    for nx, nv in bridges[now]:
      if not visited[nx] and mid <= nv:
        visited[nx] = True
        q.append(nx)
  
  return False


N, M = map(int, input().split())

bridges = [[] for _ in range(N+1)]
for i in range(M):
  A, B, C = map(int, input().split())
  bridges[A].append([B,C])
  bridges[B].append([A,C])

start, end = map(int, input().split())
low, high = 1, 1000000000

while low <= high:
  visited = [False] * (N+1)
  mid = (low+high)//2
  if bfs(start, end, mid):
    low = mid+1
  else:
    high = mid-1


print(high)