# 숫자판 점프 # B_2210
"""
5x5개의 칸에서 시작해서, 총 5번 인접한 4칸으로 이동할 수 있다.
총 25 * 4^5 = 25 * 1024 = 25,000가지의 경우의 수 존재
"""
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def go(x,y,num,len):
    if len == 6:
        ans.append(num)
        return

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<= nx < n and 0 <= ny < n:
            go(nx,ny,num*10+a[nx][ny],len+1)


n = 5
a = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        go(i,j,0,0)

ans = set(ans)
print(len(ans))

