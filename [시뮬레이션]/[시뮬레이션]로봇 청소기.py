# 로봇 청소기 # B_14503

dx = [-1,0,1,0]   # 이 문제에서만큼은 순서 중요
dy = [0,1,0,-1]   # 위 오 아 왼 (북, 동, 남, 서)
n, m = map(int, input().split())
# 0:북, 1:동, 2:남, 3:서
x, y, dir = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# a[x][y] == 0(청소하지 않은 공간)
# a[x][y] == 1(벽)
# a[x][y] == 2(청소한 공간)
while True:
    if a[x][y] == 0:
        # 현재 위치를 청소한다
        a[x][y] = 2

    # 2-3, 2-3. 네 방향 모두 청소가 되어있거나 벽인 경우
    if a[x-1][y] != 0 and a[x][y-1] != 0 and a[x][y+1] != 0 and a[x+1][y] != 0:
        # 2-4. 벽이라서 뒤로 후진할 수 없는 경우
        if a[x-dx[dir]][y-dy[dir]] == 1:
            break
        else:
            # 2-3. 바라보는 방향을 유지한 채로 한 칸을 후진하고 2번으로 돌아감
            x = x-dx[dir]
            y = y-dy[dir]
    else:
        # 2-1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음
        # 2-2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다

        dir = (dir+3) % 4  # 왼쪽으로 회전
        if a[x+dx[dir]][y+dy[dir]] == 0:
            # 2-1. 한 칸을 전진하고 1번부터 진행
            x = x+dx[dir]
            y = y+dy[dir]

ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            ans += 1

print(ans)


