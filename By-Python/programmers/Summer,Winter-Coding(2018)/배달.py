# 배달

from collections import defaultdict
import heapq 

def dijkstra(route,n,s,dest):
    heap = []
    heapq.heappush(heap,[s,0])
    dist = [float('inf')] * (n+1) #float('inf') = 양의 무한대
    dist[s] = 0

    while heap:
        node, cost = heapq.heappop(heap)
        if dist[node] < cost:
            continue
        for nd,c in route[node]: # node에서 갈 수 있는 또 다른 노드(nd)와 그때 드는 비용 c
            c += cost
            if c < dist[nd]: # 만약 현재 경로에서 nd까지 드는 비용 c가 기존 nd까지 소모되는 비용보다 작다면 갱신
                dist[nd] = c
                heapq.heappush(heap,[nd,c])
    return dist[dest]

def solution(N, road, K):
    answer = 1
    route = defaultdict(list)
    for st,de,co in road:
        route[st].append((de,co))
        route[de].append((st,co))
    
    
    for i in range(2,N+1):
        if dijkstra(route,N,1,i) <= K:
            answer += 1  

    return answer