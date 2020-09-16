# 물통 # B_2251

from collections import deque
# A,B,C가 서로에게 따를 수 있는 경우의 수 2*3=6가지
moves = list(zip([0,0,1,1,2,2], [1,2,0,2,0,1]))  # [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
ans = [False]*201  # 1~200
check = [[False]*201 for _ in range(201)]
cap = list(map(int,input().split()))  # 물통 A, B, C의 용량
sum = cap[2]  # 처음엔 C만 가득차있음
q = deque()
q.append((0,0))  # A,B는 비어있음
check[0][0] = True
ans[cap[2]] = True  # 아무에게도 따르지 않으면 될 수 있는 c의 용량
while q:
    # 현재 A,B 상태 C = sum-now[0]-now[1]
    now = q.popleft()
    # 현재 A,B,C에 담긴 물의 양
    cur = [now[0], now[1], sum-now[0]-now[1]]
    for f, t in moves:
        next = cur[:]
        next[t] += next[f]
        next[f] = 0
        if next[t] >= cap[t]:
            next[f] = next[t] - cap[t]
            next[t] = cap[t]
        if not check[next[0]][next[1]]:
            check[next[0]][next[1]] = True
            q.append((next[0],next[1]))
            if next[0] == 0:  # A가 0일때(비었을 때)
                ans[next[2]] = True  # ans[현재C의양] = True
for i in range(0, cap[2]+1):
    if ans[i]:
        print(i, end=' ')
print()


