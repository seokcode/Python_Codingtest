# 백조의 호수 # B_3197
"""
두 문제가 합쳐져 있는 문제
1. 두 백조가 만날 수 있음?/없음?
2. 각각의 얼음이 언제 녹는지(녹는시간)

day i의 얼음상태에서 백조가 만날 수 있는지 체크 -> no?
-> day i+1의 얼음상태에서 백조가 만날 수 있는지 체크 -> no?
-> day i+2의 얼음상태에서 백조가 만날 수 있는지 체크 -> yes? -> i+2 출력
"""
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())

wcheck = [[False]*m for _ in range(n)]  # 물(water)
scheck = [[False]*m for _ in range(n)]  # 백조(swan)

sx,sy,ex,ey=-1,-1,-1,-1

swan = deque()  # 지금 백조
nswan = deque()  # 다음 백조
water = deque()  # 지금 물
nwater = deque()  # 다음 물

a = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            if sx == -1:
                sx, sy = i, j  # 백조1 위치
            else:
                ex, ey = i, j  # 백조2 위치
            a[i][j] = '.'  # 위치만 기록하고 물로 표시

        if a[i][j] == '.':  # 물
            water.append((i,j))
            wcheck[i][j] = True

swan.append((sx,sy))
scheck[sx][sy] = True

i = 0
while True:
    while water:
        x,y = water.popleft()
        a[x][y] = '.'
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if wcheck[nx][ny]:
                continue
            if a[nx][ny] == '.':  # 다음 칸이 물이면 계속 갈 수 있음
                water.append((nx,ny))
                wcheck[nx][ny] = True
            else:  # 다음 칸이 얼음
                nwater.append((nx,ny))
                wcheck[nx][ny] = True
    while swan:
        x,y = swan.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if scheck[nx][ny]:
                continue
            if a[nx][ny] == '.':  # 물이면 이동 가능
                swan.append((nx,ny))
                scheck[nx][ny] = True
            else:  # 얼음이면 다음에 이동 가능(백조가 있는 곳은 물이니까)
                nswan.append((nx,ny))
                scheck[nx][ny] = True
    if scheck[ex][ey]:  # 백조가 다른 백조에게 갈 수 있는지?
        print(i)
        break
    i += 1  # day0에 못갔으면 day +1
    # 하루 지나서 녹은 얼음의 상태로 변경하고 백조의 상태도 업데이트
    water = nwater
    swan = nswan
    nwater = deque()
    nswan = deque()

