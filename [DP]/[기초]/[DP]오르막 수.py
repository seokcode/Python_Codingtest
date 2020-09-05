# 오르막 수 # B_11057

mod = 10007

n = int(input())
d = [[0]*10 for _ in range(1001)]
for i in range(0,10):
    d[1][i] = 1
for i in range(2, n+1):  # 길이
    for j in range(0, 10): # 마지막
        for k in range(0, j+1):  # 그 앞의 수
            d[i][j] += d[i-1][k]
            d[i][j] %= mod

ans = sum(d[n]) % mod
print(ans)
