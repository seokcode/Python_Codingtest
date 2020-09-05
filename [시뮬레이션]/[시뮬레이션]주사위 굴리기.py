# 시뮬레이션 B_14499
# 시뮬레이션? 문제에 나와있는것을 하나도 빠짐없이 그대로 코드로 구현하는 것

dx = [0,0,-1,1]
dy = [1,-1,0,0]
n,m,x,y,l = map(int,input().split())  # 가로,세로, x,y좌표, 이동횟수
a = [list(map(int,input().split())) for _ in range(n)]  # 도면
dice = [0]*7  # i번 면이적힌 수
move = list(map(int,input().split()))  # 이동하는 방향
# 1:동 2:서 3:북 4:남
for k in move:
    k -= 1
    # 0:동 1:서 2:북 3:남
    nx,ny = x+dx[k],y+dy[k]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    if k == 0:  # 동
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
    elif k == 1:  # 서
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
    elif k == 2:  # 남
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
    else:  # 북
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp
    x,y = nx,ny
    if a[x][y] == 0:  # 이동한 칸의 도면에 쓰여 있는 수가 0이면
        a[x][y] = dice[6]  # 주사위 바닥 면의 수를 도면에 복사
    else:  # 그렇지 않으면
        dice[6] = a[x][y]  # 주사위 바닥 면에 도면의 수를 복사
        a[x][y] = 0  # 주사위의 수 복사 후 도면의 수는 0으로 만듦

    print(dice[1])  # 이동 마다 주사위 상단에 쓰여있는 수 출력

