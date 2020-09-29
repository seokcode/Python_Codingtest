# 미네랄 # B_2933
# 교안참고(문제1)
# 미네랄 뭉텅이가 중력에 의해 내려가는 걸 구현하는게 까다로움
# 시뮬레이션 40분경 부터 시작

import sys
sys.setrecursionlimit(100000)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 그룹 짓기
def dfs(x, y, c, group):
    if a[x][y] == '.':
        return
    if c[x][y]:  # True라면 이미 한 그룹에 속해서 떨어졌다는 소리, pass
        return
    c[x][y] = True
    group.append((x,y))
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx,ny,c,group)

# 미네랄을 떨어뜨림
def simulate():
    c = [[False]*m for _ in range(n)]  # 미네랄이 땅으로 떨어졌는지 확인하기 위함(떨어졌다면 True, 더 이상 이동X)
    for x in range(n):
        for y in range(m):
            if a[x][y] == '.':  # 미네랄이 없으면 떨어뜨릴게 없음
                continue
            if c[x][y]:  # 이미 미네랄이 그룹핑이 되었고 떨어진 경우
                continue

            group = []
            dfs(x,y,c,group)  # 떨어질 때 한 뭉텅이로 떨어지는 미네랄 그룹 지어주기
            low = [-1]*m  # 각각의 열마다 한 그룹의 제일 밑이 어딘지 파악하기 위함

            for gx,gy in group:  # 미네랄이 밑으로 내려갔기때문에 빈 자리가 되는 곳 표시
                low[gy] = max(low[gy],gx)
                a[gx][gy] = '.'

            lowest = n
            for j in range(m):
                if low[j] == -1:
                    continue
                i = low[j]
                while i < n and a[i][j] == '.':
                    i += 1
                lowest = min(lowest, i-low[j]-1)
            for gx,gy in group:
                gx += lowest
                a[gx][gy] = 'x'  # 미네랄 이동
                c[gx][gy] = True  # 이동했음


n,m = map(int,input().split())  # n행 m열
a = [list(input()) for _ in range(n)]  # .은 빈칸 x는 미네랄
k = int(input())  # 막대를 던진 횟수
heights = list(map(int,input().split()))  # 1~n사이의 높이 k개

for i, height in enumerate(heights):
    height = n-height  # 인덱스의 꼭대기가 0이므로 n:8/height:6 이라면 2가 밑에서부터 6층높이를 뜻함
    # 좌,우,좌,우 순으로 막대를 던짐
    if i % 2 == 0:  # 2로 나누어 떨어지면 우측에서 던지는 순서
        for j in range(m):
            if a[height][j] == 'x':
                a[height][j] = '.'
                break
    else:  # 아니면 좌측에서 던지는 순서
        for j in range(m-1, -1, -1):
            if a[height][j] == 'x':
                a[height][j] = '.'
                break
    simulate()  # 미네랄 클러스터 뭉치가 중력에 의해 떨어지는지 확인
for row in a:
    print(''.join(row))

