# 감시 # B_15683
"""
# cctv는 최대 8가지
# 각 cctv마다 가능한 방향은 4가지,2가지,4가지,4가지,1가지
# 편의상 4가지라고 가정해도 총 가능한 경우의 수: 4^8가지 = 2^16 = 65,536
"""

# 0: 0도 회전 1: 90도 2: 180도 3: 270도
# 0번방향: → 1번방향: ↓ 2번방향: ← 3번방향: ↑
dx = [0,1,0,-1]
dy = [1,0,-1,0]


# cctv의 감시구역 표시
def check(a, b, x, y, dir):
    n = len(a)
    m = len(a[0])
    i,j = x,y
    while 0 <= i < n and 0 <= j < m:
        if a[i][j] == 6:
            break
        b[i][j] = a[x][y]
        i += dx[dir]
        j += dy[dir]


def go(a, cctv, index, dirs):
    # 모든 cctv의 회전을 결정한 경우
    # 정답 계산
    if len(cctv) == index:
        n = len(a)
        m = len(a[0])
        b = [row[:] for row in a]

        # 0번방향: → 1번방향(90): ↓ 2번방향(180): ← 3번방향(270): ↑
        for i,(what,x,y) in enumerate(cctv):
            if what == 1:  # 1번 cctv는 해당 방향 기록
                check(a,b,x,y,dirs[i])
            elif what == 2:  # 2번은 본 방향과 180도 회전 방향
                check(a,b,x,y,dirs[i])
                check(a,b,x,y,(dirs[i]+2)%4)
            elif what == 3:  # 3번은 본 방향과 90도 회전 방향
                check(a,b,x,y,dirs[i])
                check(a,b,x,y,(dirs[i]+1)%4)
            elif what == 4:  # 4번은 본 방향과 90,180도 회전 방향
                check(a,b,x,y,dirs[i])
                check(a,b,x,y,(dirs[i]+1)%4)
                check(a,b,x,y,(dirs[i]+2)%4)
            elif what == 5:  # 5번은 네 방향 전부
                check(a,b,x,y,dirs[i])
                check(a,b,x,y,(dirs[i]+1)%4)
                check(a,b,x,y,(dirs[i]+2)%4)
                check(a,b,x,y,(dirs[i]+3)%4)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if b[i][j] == 0:
                    cnt += 1
        # 사각지대 갯수 retrun
        return cnt

    ans = 100
    # ********** #
    # cctv의 회전을 결정하는 부분
    for i in range(4):
        temp = go(a, cctv, index+1, dirs+[i])
        if ans > temp:
            ans = temp  # 최솟값 저장
    return ans
    # ********* #


n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if 1 <= a[i][j] <= 5:
            cctv.append((a[i][j], i, j))  # cctv종류, 위치
print(go(a, cctv, 0, []))  # 지도, cctv, 인덱스, 방향



