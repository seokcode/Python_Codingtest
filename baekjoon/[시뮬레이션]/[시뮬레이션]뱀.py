# 뱀 # B_3190
# 뱀의 정보는 머리의 위치만 저장하면 된다.
# 머리를 제외한 나머지 칸은 머리를 쫓아가기 때문에

import sys
# 우측,아래,좌측,위
# 뱀은 처음에 오른쪽을 향한다.
dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = [[-1]*100 for _ in range(100)]  # 머리가 i,j에 몇초에 도착했는지
apple = [[False]*100 for _ in range(100)]  # 사과 위치
n = int(input())  # 보드의 크기 n*n
m = int(input())  # 사과의 개수
for _ in range(m):
    x,y = map(int,input().split())  # 사과의 위치
    apple[x-1][y-1] = True
x = 0
y = 0
direction = 0
length = 1
d[x][y] = 0
m = int(input())  # 방향 변환 정보
now = 0
# [이동, 명령(0번째)] [이동, 명령(1번째)]... [이동, 명령(m-1번째)], [이동]
# m-1번째 명령 이후를 처리하기 위해 0<=range<=m
for k in range(0, m+1):
    t = n*n+1
    ch = 'L'
    if k < m:
        t, ch = input().split()  # 초, 방향
        t = int(t)
    while now < t:  # t초에 L 혹은 D 방향으로 돌아야 함
        now += 1  # 한 칸씩 늘려나감

        # t초에 회전
        x += dx[direction]
        y += dy[direction]

        # 지도 밖으로 나가면 게임 종료
        if x < 0 or x >= n or y < 0 or y >= n:
            print(now)
            sys.exit(0)
        if apple[x][y]:  # 사과를 먹으면
            apple[x][y] = False  # 사과를 없애고 몸길이 +1
            length += 1
        # 이동하려는 칸이 예전에 머리가 방문한 칸이고 차이가 길이보다 작다면
        # 더 이상 이동할 수 없음
        if d[x][y] != -1 and now-d[x][y] <= length:
            print(now)
            sys.exit(0)
        d[x][y] = now
    # 방향 전환
    if ch == 'L':  # 왼쪽으로 90도
        direction = (direction + 3) % 4
    else:  # 오른쪽으로 90도
        direction = (direction + 1) % 4


