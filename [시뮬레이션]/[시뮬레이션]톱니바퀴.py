# 톱니바퀴 # B_14891
n = 4
a = [list(map(int, input())) for _ in range(n)]
# 0:N 1:S

k = int(input())  # 회전 횟수
for _ in range(k):
    num, direction = map(int, input().split()) # 회전할 톱니, 방향
    num -= 1
    d = [0]*n   # 각 톱니의 회전 방향 # -1:반시계 ,1: 시계
    d[num] = direction

    # 회전할 톱니의 6번과 왼쪽 톱니의 2번과 비교
    for i in range(num-1, -1, -1):
        if a[i][2] != a[i+1][6]:
            d[i] = -d[i+1]
        else:
            break
    # 회전할 톱니의 2번과 오른쪽 톱니의 6번과 비교
    for i in range(num+1, n):
        if a[i-1][2] != a[i][6]:
            d[i] = -d[i-1]
        else:
            break

    # 각 톱니별로 회전 방향이 있다면 회전시키고 없다면 그대로 두는 작업
    for i in range(n):
        if d[i] == 0:
            continue
        if d[i] == 1:
            temp = a[i][7]
            for j in range(7, 0, -1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp
        elif d[i] == -1:
            temp = a[i][0]
            for j in range(0, 7):
                a[i][j] = a[i][j+1]
            a[i][7] = temp

# 점수 환산
ans = 0
score = 1
for i in range(n):
    if a[i][0] == 1:
        ans += score
    score *= 2

print(ans)
