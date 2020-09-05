"""
그래프가 두 덩어리 이상으로 나누어져있고 덩어리 끼리 잇는 간선이 없을 때: '연결 요소'
BFS DFS 목적(임의의 한 정점에서 연결된 모든 간선 살피기)을 통해 탐색한 뒤 탐색이
종료 되면 다른 정점을 살피고 해당 정점이 이미 방문한 정점이라면 탐색을 수행하지 않고
또 다른 정점으로.. 그렇게 BFS 혹은 DFS가 실 수행 되는 횟수가 곧 연결 요소의 개수
"""
# 연결 요소 # B_11724
n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
check = [False]*(n+1)

for _ in range(m):
    u, v= map(int, input().split())
    a[u].append(v)
    a[v].append(u)

def dfs(x):
    check[x] = True
    for y in a[x]:
        if not check[y]:
            dfs(y)

ans = 0
for i in range(1, n+1):
    if not check[i]:
        dfs(i)
        ans += 1
print(ans)
