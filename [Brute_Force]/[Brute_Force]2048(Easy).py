# 2048(Easy) # B_12100
# 비트마스크
"""
# 오,왼,위,아래 4가지 방법을 최대 5번 == 4^5 = 1028가지
# 기본적인 원리는 구슬 탈출과 비슷
# 세로로 2,2,2,2를 위로 두번 이동하면 4,4 한번 더 위로 이동하면 8
"""
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
LIMIT = 5


def gen(k):
    a = [0] * LIMIT
    for i in range(LIMIT):
        a[i] = (k & 3)
        k >>= 2
    return a

# 우선 순위 정해야 함
# 위로 갈때는 위에꺼부터 합치고
# 아래로 갈때는 아래꺼부터 합치고
def check(a, dirs):
    n = len(a)
    d = [row[:] for row in a]

    for dir in dirs:
        ok = False
        merged = [[False] * n for _ in range(n)]

        while True:
            ok = False
            # 0: down, 1: up, 2: left, 3: right
            if dir == 0:
                for i in range(n - 2, -1, -1):
                    for j in range(n):
                        if d[i][j] == 0:  # 빈칸인 경우
                            continue
                        if d[i + 1][j] == 0:  # 아래가 빈칸
                            d[i + 1][j] = d[i][j]  # 현재 칸의 수와
                            merged[i + 1][j] = merged[i][j] # 정보를 아래 칸으로 넘김
                            d[i][j] = 0
                            ok = True
                        elif d[i + 1][j] == d[i][j]:  # 아래에 어떤 수가 있는 경우
                            # 둘 다 합쳐진 적이 없다면
                            if not merged[i][j] and not merged[i + 1][j]:
                                # 합침
                                d[i + 1][j] *= 2
                                merged[i + 1][j] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 1:
                for i in range(1, n):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i - 1][j] == 0:
                            d[i - 1][j] = d[i][j]
                            merged[i - 1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i - 1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i - 1][j]:
                                d[i - 1][j] *= 2
                                merged[i - 1][j] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 2:
                for j in range(1, n):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j - 1] == 0:
                            d[i][j - 1] = d[i][j]
                            merged[i][j - 1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j - 1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j - 1]:
                                d[i][j - 1] *= 2
                                merged[i][j - 1] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 3:
                for j in range(n - 2, -1, -1):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j + 1] == 0:
                            d[i][j + 1] = d[i][j]
                            merged[i][j + 1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j + 1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j + 1]:
                                d[i][j + 1] *= 2
                                merged[i][j + 1] = True
                                d[i][j] = 0
                                ok = True
            if not ok:
                break

    ans = max([max(row) for row in d])
    return ans


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for k in range(1 << (LIMIT * 2)):
    dirs = gen(k)
    cur = check(a, dirs)
    if ans < cur:
        ans = cur
print(ans)

