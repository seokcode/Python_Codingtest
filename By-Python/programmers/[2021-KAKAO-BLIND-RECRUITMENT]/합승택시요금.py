# 합승 택시 요금

# 다익스트라
from collections import defaultdict
import heapq

def dijkstra(route,n,s,e):
    heap = []
    heapq.heappush(heap,[s,0])
    dist = [float('inf')] * (n+1)
    dist[s] = 0

    while heap:
        node, cost = heapq.heappop(heap)
        if dist[node] < cost:
            continue
        for nd,c in route[node]:
            c += cost
            if c < dist[nd]:
                dist[nd] = c
                heapq.heappush(heap,[nd,c])
    return dist[e]

def solution(n, s, a, b, fares):
    route = defaultdict(list)
    for st,de,co in fares:
        route[st].append((de,co))
        route[de].append((st,co))

    answer = dijkstra(route,n,s,a) + dijkstra(route,n,s,b)
    for i in range(1,n+1):
        if s != i:
            answer = min(answer, dijkstra(route,n,s,i)+dijkstra(route,n,i,a)+dijkstra(route,n,i,b))

    return answer


# 플루이드-와샬
import heapq

def solution(n, s, a, b, fares):
    d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv
