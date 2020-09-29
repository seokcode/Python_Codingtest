# 구슬 탈출 # B_13460
# 비트마스크
"""
# 이동할 수 있는 방향이 4방향, 최대 10번 이내로 움직여야 한다.
*** 가능한 이동 방법의 수 4^10 = 1,048,576가지
# '기울인다' = 두 구슬이 움직이지 않을 때까지 기울이고 있는 것
# 즉, 같은 방향으로 두번이상 기울인 결과는 항상 같다.
*** 즉, 가능한 이동 방법의 수: 4*(4-1)^9 = 78,732가지
# 한 방향으로 이동한 다음, 반대 방향으로 바도 이동하는 것도 의미가 없다.
*** 즉, 가능한 이동 방법의 수: 4*(4-2)^9 = 2,048가지
"""

dx = [0,0,1,-1]
dy = [1,-1,0,0]
LIMIT = 10
class Result:
    def __init__(self, moved, hole, x, y):
        self.moved = moved
        self.hole = hole
        self.x = x
        self.y = y

# 정수를 4진법 수로 변환
def gen(k):
    a = [0]*LIMIT
    for i in range(LIMIT):
        a[i] = (k&3)  # == k%4
        k >>= 2  # == /4
    return a

# k라는 방향으로 기울이고 그 때 위치는 x, y
def simulate(a, k, x, y):
    n = len(a)
    m = len(a[0])
    if a[x][y] == '.':
        return Result(False, False, x, y)
    moved = False
    while True:
        nx, ny = x+dx[k], y+dy[k]  # 구슬이 어디로 이동?
        if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 구슬이 범위 내?
            return Result(moved, False, x, y)
        ch = a[nx][ny]  # 다음 칸
        if ch == '#':  # 다음 칸이 벽이라면?
            return Result(moved, False, x, y)
        elif ch in 'RB':  # 다음 칸에 구슬? == 벽
            return Result(moved, False, x, y)
        elif ch == '.':  # 길이 있다
            a[x][y],a[nx][ny] = a[nx][ny],a[x][y]  # swap(.R -> R.)
            x,y = nx,ny
            moved = True  # 움직였음
        elif ch == 'O':  # 구멍에 빠짐
            a[x][y] = '.' # 구멍에 빠져서 구슬은 사라짐
            moved = True  # 움직였음
            return Result(moved, True, x, y)

def check(a, dirs):
    n = len(a)
    m = len(a[0])
    hx,hy = 0,0
    rx,ry = 0,0
    bx,by = 0,0

    # 구멍, 빨구, 파구 위치 파악
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'O':
                hx,hy = i,j
            elif a[i][j] == 'R':
                rx,ry = i,j
            elif a[i][j] == 'B':
                bx,by = i,j

    cnt = 0
    for k in dirs:
        cnt += 1  # 몇 번 움직였는지 파악
        # hole1,2: 빨간구슬,파란구슬이 구멍에 빠졌는지 여부
        hole1 = hole2 = False
        while True:
            p1 = simulate(a, k, rx, ry)
            rx,ry = p1.x, p1.y
            p2 = simulate(a, k, bx, by)
            bx,by = p2.x, p2.y

            # 빨간, 파란 구슬이 움직이지 않았으면 기울이는것을 그만 둠
            if not p1.moved and not p2.moved:
                break
            if p1.hole:  # 빨간구슬이 구멍에 빠졌는지?
                hole1 = True
            if p2.hole:  # 파란구슬이 구멍에 빠졌는지?
                hole2 = True

        if hole2:  # 파란 구슬이 빠졌다면 불가능
            return -1
        if hole1: # 빨간 구슬이 빠졌다면
            return cnt

    return -1

def valid(dirs):
    l = len(dirs)
    for i in range(l-1):
        # 반대 방향의 경우 제거
        if dirs[i] == 0 and dirs[i+1] == 1:
            return False
        if dirs[i] == 1 and dirs[i+1] == 0:
            return False
        if dirs[i] == 2 and dirs[i+1] == 3:
            return False
        if dirs[i] == 3 and dirs[i+1] == 2:
            return False
        # 같은 방향의 경우 제거
        if dirs[i] == dirs[i+1]:
            return False
    return True

n,m = map(int,input().split())  # 세로, 가로
original = [input() for _ in range(n)]  # 구슬 지도
ans = -1
for k in range(1<<(LIMIT*2)):  # 모든 경우의 수 4^10 = 2^20
    dirs = gen(k)
    if not valid(dirs):
        continue
    a = [list(row) for row in original]
    cur = check(a, dirs)
    if cur == -1:
        continue
    if ans == -1 or ans > cur:
        ans = cur

print(ans)

