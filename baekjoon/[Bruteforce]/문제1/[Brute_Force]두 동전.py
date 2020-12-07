# 두 동전 # B_16197
"""
4개의 버튼 10번보다 많이 누르면 -1 출력
총 4개의 방향을 최대 10번까지 수행할 수 있음
4^10 = 1,048,576
"""

def go(step,x1,y1,x2,y2):
    if step == 11:  # 동전 이동 횟구가 10번을 초과하면 실패
        return -1

    fall1 = False
    fall2 = False
    if x1 >= n or x1 < 0 or y1 >= m or y1 < 0:  # 동전1이 떨어짐
        fall1 = True
    if x2 >= n or x2 < 0 or y2 >= m or y2 < 0:  # 동전2가 떨어짐
        fall2 = True

    if fall1 and fall2:  # 둘 다 떨어지면 실패
        return -1
    if fall1 or fall2:  # 둘 중 하나만 떨어짐 step 반환
        return step

    ans = -1
    for k in range(4):
        nx1, ny1 = x1+dx[k] , y1+dy[k]
        nx2, ny2 = x2 + dx[k], y2 + dy[k]
        # 벽이 있으면 못감
        if 0 <= nx1 < n and 0 <= ny1 < m and a[nx1][ny1] == '#':
            nx1,ny1 = x1,y1
        if 0 <= nx2 < n and 0 <= ny2 < m and a[nx2][ny2] == '#':
            nx2,ny2 = x2,y2


        temp = go(step+1,nx1,ny1,nx2,ny2)
        if temp == -1:
            continue
        if ans == -1 or ans > temp:
            ans = temp
    return ans


dx = [0,0,-1,1]
dy = [-1,1,0,0]

n, m = map(int, input().split())
x1=y1=x2=y2= -1
a = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] == 'o':  # 동전 위치 표시
            if x1 == -1:
                x1, y1 = i,j
            else:
                x2,y2 = i,j

print(go(0,x1,y1,x2,y2))