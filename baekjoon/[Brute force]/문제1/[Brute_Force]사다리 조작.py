# 사다리 조작 # B_15684
"""
세로선의 개수 2<= N <=10
세로선마다 가로선을 놓을 수 있는 위치의 개수 1<= H <=30
가로선의 개수 0<= M <=(N-1)*H
-> 총 경우의수 2^(N-1)H

정답이 3보다 크거나 불가능하면 -1
-> 연구소 문제와 비슷하게 3보다 크면 전부 답이 안되기 때문에 경우의 수가 확 줄게 된다
    즉, 전체 경우의 수는 (N-1)*H개 중에서 3개를 고르는 경우의 수와 같다
    -> 9*30=270개중에 사다리를 3개까지만 놓는 경우의 수 = 270^3

1*----*2 사다리의 왼쪽은 1 오른쪽은 2를 적고 없는 곳은 0을 적어서 시뮬레이션 진행
"""
import sys


def start(c):
    r = 1
    while r <= h:
        # garo[r][c] == 1 -> (r,c) 와 (r,c+1)이 연결
        if garo[r][c] == 1:
            c += 1
        # garo[r][c] == 2 -> (r,c-1) 와 (r,c)이 연결
        elif garo[r][c] == 2:
            c -= 1
        r += 1  # 한칸씩 내려감 연속으로 좌측 혹은 우측으로 가는 경우는 없음
    return c  # 사다리 번호 return


def go():
    # 1번 사다리부터 차례대로 체크
    for i in range(1, w):
        res = start(i)
        if res != i:  # 최종 도착 사다리 번호가 출발했던 사다리 번호랑 안같으면
            return False
    return True


w,m,h = map(int, input().split())  # 세로선, 가로선, 추가할 수 있는 가로선
garo = [[0]*(w+1) for _ in range(h+1)]

# 이미 있는 가로 선 입력
for _ in range(m):
    x, y = map(int, input().split())
    garo[x][y] = 1
    garo[x][y+1] = 2

a = []
for i in range(1, h+1):
    for j in range(1,w):
        if garo[i][j] != 0:
            continue
        if garo[i][j+1] != 0:
            continue
        # 사다리를 놓을 수 있는 곳이면 append
        a.append((i, j))

# 기본 값에서 별도의 사다리를 추가하지 않아도 정답이 된다면 종료
if go():
    print(0)
    sys.exit(0)

ans = -1
for i in range(len(a)):
    x1, y1 = a[i]

    if garo[x1][y1] != 0 or garo[x1][y1+1] != 0:
        continue
    garo[x1][y1] = 1
    garo[x1][y1+1] = 2
    if go():  # 사다리를 하나만 추가했을 떄 답이 되는 경우
        if ans == -1 or ans > 1:
            ans = 1

    for j in range(i + 1, len(a)):
        x2, y2 = a[j]
        if garo[x2][y2] != 0 or garo[x2][y2 + 1] != 0:
            continue
        garo[x2][y2] = 1
        garo[x2][y2 + 1] = 2
        if go():  # 사다리를 두개 추가했을 떄 답이 되는 경우
            if ans == -1 or ans > 2:
                ans = 2

        for k in range(j + 1, len(a)):
            x3, y3 = a[k]
            if garo[x3][y3] != 0 or garo[x3][y3 + 1] != 0:
                continue
            garo[x3][y3] = 1
            garo[x3][y3 + 1] = 2
            if go():  # 사다리를 세개 추가했을 떄 답이 되는 경우
                if ans == -1 or ans > 3:
                    ans = 3
            garo[x3][y3] = 0
            garo[x3][y3 + 1] = 0
        garo[x2][y2] = 0
        garo[x2][y2 + 1] = 0
    garo[x1][y1] = 0
    garo[x1][y1 + 1] = 0
print(ans)