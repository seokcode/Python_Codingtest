# 종이 조각 # B_14319
# 비트마스크

n, m = map(int, input().split())  # n:세로, m:가로
a = [list(map(int, list(input()))) for _ in range(n)]
ans = 0

# 1<<(n*m) == 2^n*m
# 각 칸은 가로나 세로(2가지)에 속할 수 있다
for s in range(1<<(n*m)):
    # 하나의 s에 대해서 가로,세로 최댓값을 ans 에 저장하고,
    # 다음 s에 대해서 sum=0으로 시작
    sum = 0
    # 가로에 대해서 계산
    for i in range(n):
        cur = 0  # 현재 수가 몇인지
        for j in range(m):
            k = i*m+j  # 0*m+0 = 첫번째 칸 0*m+1 = 두번째 칸
            if (s&(1<<k)) == 0:  # 해당 칸이 가로라면
                cur = cur * 10 + a[i][j]
            else:  # 해당 칸이 세로일 때
                # 세로가 나왔다는건 계산중인 가로가 끝났음을 의미하므로
                # sum에 더해주고 cur=0으로 초기화
                sum += cur
                cur = 0
        sum += cur

    # 세로에 대해서 계산
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m+j
            if (s&(1<<k)) != 0:
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)
print(ans)