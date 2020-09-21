# 스타트링크 # B_5014
"""
기회 비용 1 최솟값 구하는 문제 -> BFS
"""
from collections import deque

# 총 f층으로 이루어진 건물, g층으로 가아하고 현재 s층에 있음
# 엘레베이터에는 u개 층만큼 올라갈 수 있는 버튼과 d개 층만큼 내려갈 수 있는 버튼 존재
f, s, g, u, d = map(int, input().split())
dist = [0] * (f+1)  # 버튼 누른 횟수
check = [False] * (f+1)  # 방문 체크
check[s] = True
q = deque()
q.append(s)

while q:
    now = q.popleft()

    # u 버튼을 눌러서 올라간 곳이 건물 꼭대기 층수 이하이고 방문한 적 없는 곳이라면
    if now + u <= f and not check[now+u]:  # 순서 주의
        dist[now+u] = dist[now] + 1
        check[now+u] = True
        q.append(now+u)
    # d 버튼을 눌러서 내려간 곳이 1층 이상이고 방문한 적 없는 곳이라면
    if now - d >= 1 and not check[now-d]:
        dist[now-d] = dist[now] + 1
        check[now - d] = True
        q.append(now-d)

if check[g]:
    print(dist[g])
else:
    print("use the stairs")

