from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    dq = deque()
    # 1번 노드에서 시작, 1번 노드는 거리 0
    dq.append([1,0])
    
    # 양방향이기 때문에 양방향 저장
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
        
    while dq:
        node, depth = dq.popleft()
        
        for next in graph[node]:
            # 방문한 적이 없다면?
            if visited[next] == 0:
                # depth + 1 하여 다음 방문할 노드로 append
                visited[next] = depth+1
                dq.append([next,depth+1])
        
    # 출발 노드는 카운트에서 제외
    visited[1] = 0
    return visited.count(max(visited))