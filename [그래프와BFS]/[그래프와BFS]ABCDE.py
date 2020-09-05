"""
# BFS가 그래프 알고리즘이기 때문에 그래프와 BFS를 같이 배운다
# 공간복잡도: '인접행렬'(O(V^2)), '인접리스트'(O(E))
# 대부분의 경우 '인접리스트'가 훨씬 빠름
# 하지만 인접 행렬이 좋을 때
## 1. 두 정점 u,v가 주어졌을 때 u->v로 가는 방법이 존재하는지를 찾을 때
## A[u][v]를 찾으면 됨: O(1)만큼 걸려서 빠름
## 2. 두 정점 u,v가 주어졌을 때 v->u로 가는 방법이 존재하는지를 찾을 때
## A[v][u]를 찾으면 됨: O(1)만큼 걸려서 빠름
# 완전 그래프: 모든 정점(node, vertex) 사이에 간선(edge)이 존재하는 것
# 완전 그래프의 경우에서는 '인접 행렬'이 가장 좋음 하지만 문제로 많이 출제되진 않음
"""
# ABCDE # B_13023
# 전형적인 DFS 문제이다.
# 문제의 요점은 A-B, B-C, C-D, D-E인 친구관계가 존재하는지를 조사하는 것이다.
n, m = map(int, input().split())
visited = [False for _ in range(n)]
adj = [[] for _ in range(n)]

# 인접리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(v, depth):
    global ans
    visited[v] = True
    if depth == 4:
        ans = True
        return
    for i in adj[v]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False

ans = False
for k in range(n):
    dfs(k,0)
    visited[k] = False
    if ans:
        break

print(1 if ans else 0)
"""
import sys
n, m = map(int, input().split())
edges = []
a = [[False]*n for _ in range(n)]
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    edges.append((v, u))
    a[u][v] = a[v][u] = True
    g[u].append(v)
    g[v].append(u)
print(edges)
print(g)
m *= 2
for i in range(m):
    for j in range(m):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not a[B][C]:
            continue
        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit(0)
print(0)
"""


