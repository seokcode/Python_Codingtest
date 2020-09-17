# 과외맨 # B_5213
"""
# 홀수 열은 n개의 타일(한 타일은 두 조각으로 이루어짐) 짝수열은 n-1개 타일
# 그림을 그리고 2차원 배열로 생각하여 해결
"""
from collections import deque
# 홀수 열 (0번 인덱스 부터 시작해서 코드에서는 짝수열로 취급)
# 왼쪽왼 위 대각,오른 위 대각, 오른, 오른 아래 대각, 왼 아래 대각[6방향]
dx0 = [-1,-1,0,1,1,0]
dy0 = [-1,0,1,0,-1,-1]

# 짝수 열 (0번 인덱스 부터 시작해서 코드에서는 홀수열로 취급)
# 왼쪽왼 위 대각,오른 위 대각, 오른, 오른 아래 대각, 왼 아래 대각[6방향]
dx1 = [-1,-1,0,1,1,0]
dy1 = [0,1,1,1,0,-1]

dx = [dx0,dx1]  # x%2==0이면 홀수열이므로 앞에꺼 아니면 짝수열이므로 뒤에꺼
dy = [dy0,dy1]


# 갈 수 있는 곳인지 체크
def ok(x,y):
    if x < 0 or x >= n:
        return False
    if x % 2 == 0:  # 0,2,4...번 인덱스(홀수열)
        return y >= 0 and y < n  # n개의 열 존재
    else:  # 짝수열
        return y >= 0 and y < n-1  # n-1개의 열 존


def go(x1,y1,x2,y2):
    if x1 == x2:  # 행이 같은 경우(바로 옆으로 이동), (*0->0*) 0에 있는 숫자가 같아야 함
        if y1 < y2:
            return a[x1][y1][1] == a[x2][y2][0]
        else:
            return a[x1][y1][0] == a[x2][y2][1]

    else:  # 다른 행에 있는 경우
        if x1%2 == 0: # x1이 0,2,4...번 인덱스(홀수열)
            if y1 == y2:
                return a[x1][y1][1] == a[x2][y2][0]
            else:
                return a[x1][y1][0] == a[x2][y2][1]
        else: # 짝수열
            if y1 == y2:
                return a[x1][y1][0] == a[x2][y2][1]
            else:
                return a[x1][y1][1] == a[x2][y2][0]


def num(x, y):
    ans = x//2*(n*2-1)
    if x%2 == 1:
        ans += n
    ans += y+1
    return ans


n = int(input())
a = [[] for _ in range(n)]
for i in range(n):
    lim = n if i%2 == 0 else n-1  # 홀수열(0,2,4..)은 n개 짝수열은 n-1개 타일
    for j in range(lim):
        a[i].append(tuple(map(int,input().split())))  # 타일 구성

q = deque()
check = [[False]*n for _ in range(n)]  # 방문 체크
dist = [[False]*n for _ in range(n)]  # 이동 횟수
via = [[-1]*n for _ in range(n)]  # 경로 체크
check[0][0] = True  # 시작 지점
dist[0][0] = 1
q.append((0, 0))

while q:
    x, y = q.popleft()
    for k in range(6):
        # x%2==0이면 홀수열이므로 앞에꺼 아니면 짝수열이므로 뒤에꺼
        nx, ny = x+dx[x%2][k], y+dy[x%2][k]
        if not ok(nx,ny):  # 갈 수 없는 곳이면 continue
            continue
        if not go(x, y, nx, ny):
            continue
        if check[nx][ny]:  # 방문했던 곳이면 continue
            continue
        check[nx][ny] = True
        dist[nx][ny] = dist[x][y] + 1  # 이동 횟수 갱신
        via[nx][ny] = (x, y)  # 온 경로 기록
        q.append((nx, ny))

# 문제에서 마지막 타일로 가지 못하면 최대한 번호가 큰 타일까지 가라고 했기 떄문
# 2차원 배열의 끝부터 방문한 타일 중 가장 번호가 큰 것을 저장
# -> # ****경로 표시**** 에서 해당 인덱스부터 경로 추적할 수 있도록
x = n-1
y = n-1
while not check[x][y]:
    y -= 1
    if y < 0:
        x -= 1
        y = n-1
        if x % 2 == 1:
            y -= 1

print(dist[x][y])

# ****경로 표시****
s = []
while not (x == 0 and y == 0):
    s.append((x,y))
    x, y = via[x][y]
s.append((x,y))

while s:
    print(num(*s[-1]), end=' ')
    s.pop()
print()
# ****경로 표시****
