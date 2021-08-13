# DFS와 BFS # B_1260
from collections import deque
n, m, start = map(int,input().split())
a = [[] for _ in range(n+1)]
check = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

# 한 노드에 연결된 간선 오름차순 정렬
for i in range(n):
    a[i].sort()

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for y in a[x]:
        if not check[y]:
            dfs(y)

def bfs(start):
    check = [False]*(n+1)  # 초기화
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if not check[y]:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()