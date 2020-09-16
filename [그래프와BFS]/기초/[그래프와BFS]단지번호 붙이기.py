"""
플러드 필: 어떤 위치와 연결된 '모든 위치'를 찾는 알고리즘
연결 요소를 찾는 문제와 유사 문제됨(즉, 연결요소 연습 문제)
하지만 인접리스트 혹은 인접행렬을 만들지 않아도 됨 -> 이미 2차원 배열이기 때문
"""
# 단지번호붙이기 # B_2667
import sys
from collections import deque,Counter
from functools import reduce
# dx:행, dy:열
# 갈 수 있는 방향을 나타냄
# 오른, 왼, 아래, 위
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x, y, cnt):
    q = deque()
    # 현 위치 큐에 push
    q.append((x,y))
    group[x][y] = cnt
    # 큐에 값이 있는 동안 반복
    while q:
        # 현 위치 큐에서 pop
        x, y = q.popleft()
        for k in range(4):
            # 자신의 위치 기준 상하좌우로 집이 있는지 있다면 방문했던 곳인지 검사
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    # 집이 있고 방문하지 않았었다면
                    # q에 해당 위치 push(해당 위치로부터 상하좌우 검사)
                    q.append((nx, ny))
                    # 해당 위치에 현재 cnt(그룹번호) 부여
                    group[nx][ny] = cnt


n = int(sys.stdin.readline())
a = [list(map(int, list(input()))) for _ in range(n)]
group = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            # cnt 값이 +1 된다는 것은 한 그룹의 탐색이 종료되었음을 의미
            cnt += 1
            bfs(i, j, cnt)

# group('[[]]형식')을 단일리스트로 저장
ans = reduce(lambda x,y : x+y, group)
# group에서 0보다 큰. 즉, 집들만(1,2,3...) 저장
ans = [x for x in ans if x>0]
# 1의 갯수, 2의 갯수.. 즉, 단지 내 집의 갯수를 count
ans = sorted(list(Counter(ans).values()))

print(cnt)
print('\n'.join(map(str, ans)))

"""
# dfs코드

from collections import deque, Counter
from functools import reduce
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x, y, cnt):
    group[x][y] = cnt
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 1 and group[nx][ny] == 0:
                dfs(nx, ny, cnt)
n = int(input())
a = [list(map(int,list(input()))) for _ in range(n)]
group = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            dfs(i, j, cnt)

ans = reduce(lambda x,y : x+y, group)
ans = [x for x in ans if x > 0]
ans = sorted(list(Counter(ans).values()))
print(cnt)
print('\n'.join(map(str,ans)))
"""