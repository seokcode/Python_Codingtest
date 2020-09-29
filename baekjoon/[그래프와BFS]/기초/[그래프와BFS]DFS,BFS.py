"""
# DFS/BFS(탐색)알고리즘의 목적
임의의 시작점 x에서 시작하여 모든 정점을 한번씩것만 방문하는 것

# DFS: 한 시작점에서 갈 수 있을때까지 계속 진행 끝까지 갔으면 뒤로 돌아서 끝까지 진행
## 스택, 재귀함수를 이용 / 스택에 방문 표시 / 스택이 다시 비게 되면 탐색 종료

# BFS: 한 시점에서 갈 수 있는 곳을 동시에 진행(쭉쭉 뻗어가는 모습)
# 큐를 이용 / 큐에 방문 표시 / 한 노드의 간선을 파악 헀으면 pop/ 큐가 비게 되면 탐색 종료

## DFS/BFS의 '인접 행렬' 시간 복잡도: 정점의 개수 * 함수의 호출 갯수 : O(V^2)
## DFS/BFS의 '인접 리스트' 시간 복잡도: O(V+E)
"""
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