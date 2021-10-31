from collections import defaultdict, deque

def solution(n, wires):
    def bfs(node, a,b):
        q = deque([node])
        visit = [False] * (n+1)
        visit[node] = True
        cnt = 1
        
        while q:
            cur = q.popleft()
            for i in wire[cur]:                
                if (cur == a and i == b) or (cur == b and i == a):
                    continue
                if not visit[i]:
                    visit[i] = True
                    q.append(i)
                    cnt += 1
        return cnt 
                
        
    wire = defaultdict(list)    
    for a,b in wires:
        wire[b].append(a)
        wire[a].append(b)
    
    answer = 10000000
    for a,b in wires:
        group_one = bfs(1,a,b)
        group_two = n-group_one
        answer = min(answer, abs(group_one - group_two))

    return answer