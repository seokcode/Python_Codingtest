# 숨바꼭질2 # B_12851
"""
# 최단 이동경로의 수 # BFS+DP
# 숨바꼭질 # B_1697
# 동생을 찾는 가장빠른시간을 구하는 문제(BFS)
"""
from collections import deque
MAX = 200000
check = [False]*MAX
dist = [0]*MAX
cnt = [0]*MAX  # cnt[i] = i까지 가는 방법의 개수

n, m = map(int, input().split())
check[n] = True
dist[n] = 0  # 걸리는 시간 계산
cnt[n] = 1
q = deque()
q.append(n)

while q:
    now = q.popleft()
    for next in [now-1, now+1, now*2]:
        if 0 <= next < MAX:
            if not check[next]:
                check[next] = True  # 방문했음을 표시
                dist[next] = dist[now] + 1  # 걸리는 시간 계산
                q.append(next)
                cnt[next] = cnt[now]
            # 방문은 했지만 최단시간의 경로가 하나 더 있을 경우
            # 다음 목적지까지 1이라는 시간만 더 걸려야 최단거리
            elif dist[next] == dist[now] + 1:
                cnt[next] += cnt[now]

print(dist[m])
print(cnt[m])
