# 드래곤 커브 # B_15685
"""
# (0,0)에서 오른쪽 방향으로 시작한 1세대 드래곤 커브
# 다음 세대는 이전 세대를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음 그 곳에 붙인
"""
c = [[False]*101 for _ in range(101)]
# 오른, 위, 왼, 아래
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 회전방향 반환
def curve(x,y,dir,gen):
    ans = [dir]
    for g in range(1, gen+1):
        temp = ans[:]
        temp = temp[::-1]  # 역순 # 왜?
        # 회전 시킨 후 방향을 반대로 해야 본래 좌표에서 해당 방향으로 이동했을 때 해당 좌표와 일치
        for i in range(len(temp)):
            temp[i] = (temp[i]+1)%4  # 0:오 1:위: 2:왼 3:아
        ans += temp
    return ans


n = int(input())  # 드래곤 커브의 갯수
for _ in range(n):
    """
    방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.
    0: x좌표가 증가하는 방향 (→)
    1: y좌표가 감소하는 방향 (↑)
    2: x좌표가 감소하는 방향 (←)
    3: y좌표가 증가하는 방향 (↓)
    
    # x축은 → y축은 ↓
    """
    y,x,dir,gen = map(int,input().split())
    dirs = curve(x,y,dir,gen)
    c[x][y] = True
    for d in dirs:
        x += dx[d]
        y += dy[d]
        c[x][y] = True  # 드래곤 커브에 포함된 좌표
ans = 0
for i in range(100):
    for j in range(100):
        # 네 꼭짓점이 드래곤 커브에 포함되어 있는지?
        if c[i][j] and c[i][j+1] and c[i+1][j] and c[i+1][j+1]:
            ans += 1
print(ans)

