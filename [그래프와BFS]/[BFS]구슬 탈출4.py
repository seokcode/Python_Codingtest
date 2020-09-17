# 구슬 탈출4 # B_15653
# 총 가능한 상태의 개수 (NM)^2 = 정점의 개수

from collections import deque
import copy
dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()


def simulate(a, k, x, y):
    if a[x][y] == '.':
        return False, False, x, y
    n = len(a)
    m = len(a[0])
    moved = False
    while True:
        nx, ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 칸 초과
            return moved, False, x, y

        if a[nx][ny] == '#':  # 이동하려는 칸이 벽
            return moved, False, x, y

        elif a[nx][ny] in 'RB':  # 빨강 혹은 파랑구슬이 앞에 있음
            return moved, False, x, y

        elif a[nx][ny] == '.':  # 빈칸
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]  # 이동
            x, y = nx, ny  # 이동
            moved = True  # 이동했음을 표시

        elif a[nx][ny] == 'O':  # 구멍
            a[x][y] = '.'  # 구멍에 빠졌으니 현재 있던 칸은 빈칸
            moved = True  # 이동했음을 표시
            return moved, True, x, y


def go(b, rx, ry, bx, by, direction):
    a = copy.deepcopy(b)  # 그냥 복사 시 원본이 동시 수정됨을 막기 위해 deepcopy
    a[rx][ry] = 'R'
    a[bx][by] = 'B'
    hole1 = False
    hole2 = False
    while True:  # 빨강과 파랑 구슬이 움직이지 않을때까지 기울임 연산 반복
        # 움직였는지, 구멍에 빠졌는지
        rmoved, rhole, rx, ry = simulate(a, direction, rx, ry)
        bmoved, bhole, bx, by = simulate(a, direction, bx, by)
        if not rmoved and not bmoved:  # 둘 다 구슬이 움직이지 않음 -> 그만 움직여도 됨
            break

        # 구멍에 빠진 경우
        if rhole:
            hole1 = True
        if bhole:
            hole2 = True

    return hole1, hole2, rx, ry, bx, by


n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
# 4차원 배열
d = [[[[-1]*m for k in range(n)] for j in range(m)] for i in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'R':  # 빨강구슬 위치
            rx = i
            ry = j
            a[i][j] = '.'
        elif a[i][j] == 'B':  # 파랑구슬 위치
            bx = i
            by = j
            a[i][j] = '.'
        elif a[i][j] == '0':  # 구멍 위치
            hx = i
            hy = j
q.append((rx,ry,bx,by))
d[rx][ry][bx][by] = 0  # 이동을 하나도 안했으니까 0
found = False

while q:
    rx, ry, bx, by = q.popleft()
    for k in range(4):
        # a 배열과 현재 위치, 방향인덱스(dx,dy)의 번호를 인자로 넣음
        hole1, hole2, nrx, nry, nbx, nby = go(a, rx, ry, bx, by, k)
        if hole2:  # 파란구슬이 빠졌을 떄, 건너 뜀
            continue
        if hole1:  # 빨강구슬이 빠졌을 때
            found = True  # 정답 찾음
            ans = d[rx][ry][bx][by] + 1  # 지금까지 이동한 횟수+1
            break  # 반복 종료
        if d[nrx][nry][nbx][nby] != -1:  # 구슬을 이동시켰는데 이미 방문했던 곳이라면, 건너 뜀
            continue

        q.append((nrx, nry, nbx, nby))  # 다음 반복을 위해 push
        d[nrx][nry][nbx][nby] = d[rx][ry][bx][by] + 1  # 이동 횟수 증가
    if found:
        break  # while문 종료

print(ans)
