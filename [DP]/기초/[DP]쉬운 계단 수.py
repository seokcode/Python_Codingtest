# 쉬운 계단 수 # B_10844
# D[N][L] = 길이가 N, 마지막 수 L 인 계단 수
# D[N][L] = D[N-1][L-1] + D[N-1][L+1] (단, L = 0 or 9인 경우 예외처리)
mod = 1000000000

n = int(input())
d = [[0]*10 for _ in range(101)]
for i in range(1,10):
    d[1][i] = 1
for i in range(2,n+1):
    for j in range(0,10):
        d[i][j] = 0
        if j-1 >= 0:
            d[i][j] += d[i-1][j-1]
        if j+1 <= 9:
            d[i][j] += d[i-1][j+1]
        d[i][j] %= mod

ans = 0
ans = sum(d[n]) % mod
print(ans)
