# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 # B_2422

n, m = map(int,input().split())
d = [[False]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    d[a-1][b-1] = d[b-1][a-1] = True  # 맛 없는 조합

ans = 0

# 순서만 다른 선택지는 다른 선택지가 아니다
for i in range(0,n-2): # 1~10의 범위일 경우 첫 번째 선택에서는 1~8까지만 골라야 9,10을 고를 수 있음
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if d[i][j] or d[i][k] or d[j][k]:  # 맛 없는 조합일 경우
                continue
            ans += 1

print(ans)