"""
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록
분할할 수 있을 때,그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
"""

# 이분 그래프 # B_1707
# 색으로 분류하는 방법
import sys
sys.setrecursionlimit(1000000)
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = [[] for _ in range(n)]
    color = [0] * n  # 0:방문x, 1:그룹A, 2:그룹B
    # 인접 리스트 생성(모든 정점은 1부터 시작하므로 인덱스 특성 상 -1)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        a[u-1].append(v-1)
        a[v-1].append(u-1)

    # node x를 c로 색칠하라
    # 3-c? c->3-c가 되면 1->2, 2->1이됨
    def dfs(x, c):
        color[x] = c
        for y in a[x]:
            if color[y] == 0:
                if not dfs(y, 3-c):
                    return False
            elif color[y] == color[x]:
                return False
        return True

    ans = True
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                ans = False
    print('YES' if ans else 'NO')
