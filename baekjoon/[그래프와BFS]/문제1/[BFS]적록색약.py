# 적록색약 # B_10026

from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 적록색약일때의 경우를 처리하기 위한 함수
def can(blind, u, v):
    if u == v:
        return True
    if blind:
        if u == 'R' and v == 'G':
            return True
        if u == 'G' and v == 'R':
            return True
    return False


def go(a, blind):
    n = len(a)
    check = [[False]*n for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            if check[i][j]:
                continue
            # else:새로운 그룹
            ans += 1
            q = deque()
            q.append((i, j))
            check[i][j] = True

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if check[nx][ny]:
                            continue
                        if can(blind, a[x][y], a[nx][ny]):
                            check[nx][ny] = True
                            q.append((nx, ny))

    return ans


n = int(input())
a = [input() for _ in range(n)]
print(str(go(a, False)) + ' ' + str(go(a, True)))  # 정상인이 보는 구역 갯수 적록색약인 사람이 본 구역의 갯수
