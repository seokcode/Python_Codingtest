# 견우와 직녀 # B_16137
# 오작교를 추가로 하나 더 만들 수 있음

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = -1


def bfs():
    dist = [[[-1]*20 for j in range(n)] for i in range(n)]  # 주기 최댓값 20
    q = deque()
    q.append((0,0,0))
    dist[0][0][0] = 0
    while q:
        x, y, t = q.popleft()

        # 현재 밝고 있는 칸이 >= 2 이면 오작교
        # 현재까지 걸린 시간이 a[x][y]의 배수가 아니라면 건널 수 없음
        if a[x][y] >= 2 and t % a[x][y] != 0:

            # 현재 위치에서 시간만 추가
            nt = (t+1) % a[x][y]
            if dist[x][y][nt] == -1:
                dist[x][y][nt] = dist[x][y][t] + 1
                q.append((x,y,nt))
        else:
            for k in range(4):
                nx,ny = x+dx[k], y+dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    # 현재 밝고 있는 곳도 밟을 곳도 오작교일 경우
                    # 오작교는 두번 연속 건널 수 없음
                    if a[x][y] >= 2 and a[nx][ny] >= 2:
                        continue

                    # 벽이 아니면 건넘
                    if a[nx][ny] >= 1:
                        nt = (dist[x][y][t]+1) % a[nx][ny]
                        if dist[nx][ny][nt] == -1:
                            dist[nx][ny][nt] = dist[x][y][t] + 1
                            q.append((nx, ny, nt))
    ans = -1
    for i in range(20):
        if dist[n-1][n-1][i] == -1:
            continue
        if ans == -1 or ans > dist[n-1][n-1][i]:
            ans = dist[n-1][n-1][i]
    return ans


# 추가로 설치할 오작교는 절벽이 교차하는 지점에는 안됨
# can(i,j)가 둘 다 True면 못 놓는 것
def can(i, j):
    # 좌,우 0(절벽)인지 체크
    garo = False
    if j-1 >= 0 and a[i][j-1] == 0:
        garo = True
    if j+1 < n and a[i][j+1] == 0:
        garo = True

    # 상,하 0(절벽)인지 체크
    sero = False
    if i-1 >= 0 and a[i-1][j] == 0:
        sero = True
    if i+1 < n and a[i+1][j] == 0:
        sero = True

    return not (garo and sero)
    # and연산: 둘 다 참일 때만 True
    # 여기서는 not이 있으니까 둘 다 참일때만 False


for i in range(n):
    for j in range(n):
        if a[i][j] == 0 and can(i, j):
            a[i][j] = m  # 오작교 넣고
            now = bfs()  # bfs 실행
            if now != -1:
                if ans == -1 or ans > now:
                    ans = now  # 오작교를 놓는 여러 경우 중 최솟값 구하기
            a[i][j] = 0
print(ans)


