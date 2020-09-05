# 1학년 # B_5557
"""
# +,-(2가지) -> 2^n가지 = 2^100이라서 많은 경우의 수가 있지만
# 0~20까지의 범위가 있음
# d[i][j] = i까지의 합이 j인 식의 갯수
# d[i][j] = d[i-1][j-a[i]] + d[i-1][j+a[i]]
# 8 3 2 4 8 7 2 4 0 8 (=) 8 에서 숫자는 총 n-1개 연산자는 n-2개
"""
n = int(input()) - 1 # 마지막 수('=8')는 계산되는 수가 아니기 때문
a = [0] + list(map(int, input().split()))
goal = a[-1]
a = a[:-1]
d = [[False]*21 for _ in range(n)]  # 상근이는 20을 넘는 수는 모름
d[0][a[0]] = 1
for i in range(1,n):
    for j in range(21):
        if j-a[i] >= 0:
            d[i][j] += d[i-1][j-a[i]]
        if j+a[i] <= 20:
            d[i][j] += d[i-1][j+a[i]]

print(d[n-1][goal])
