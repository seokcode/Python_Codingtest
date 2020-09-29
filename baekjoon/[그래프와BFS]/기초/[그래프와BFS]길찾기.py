# 안전 영역 # B_2468
# 단지번호 붙이기 + 섬의 개수

from collections import deque
from functools import reduce

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(x, y, cnt, height):
    q = deque()
    q.append((x, y))
    group[x][y] = cnt

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] > height and group[nx][ny] == 0:
                    # 강수량보다 건물 높이가 높고 방문하지 않았었다면
                    # q에 해당 건물 push(해당 위치로부터 상하좌우 검사)
                    q.append((nx, ny))
                    # 해당 건물에 현재 cnt(그룹번호) 부여
                    group[nx][ny] = cnt


n = int(input())
a = [list(map(int, list(input().split()))) for _ in range(n)]

ans = reduce(lambda x,y : x+y, a)  # group('[[]]형식')을 단일리스트로 저장
ans = [x for x in ans if x>0]  # group에서 0보다 큰. 즉, 집들만(1,2,3...) 저장
ans = set(ans)  # 중복 값 제거
q = deque()

solution = []  # 강수량에 따른 cnt 저장(해당 리스트의 최댓값이 답)
for height in range(max(ans)+1):  # 0부터 최대 건물 높이까지 강수량 증가
    cnt = 0
    group = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] > height and group[i][j] == 0:
                # cnt 값이 +1 된다는 것은 한 그룹의 탐색이 종료되었음을 의미
                cnt += 1
                bfs(i, j, cnt, height)
    solution.append(cnt)

print(max(solution))
