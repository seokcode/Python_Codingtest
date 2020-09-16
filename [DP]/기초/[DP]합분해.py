# 합분해 # B_2225
# 1,2,3 더하기와 비슷
"""
# D[K][N] = 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
# 마지막 수: L
# D[K][N] = sigma.D[K-1][N-L] (단, 문제에 의하면 0 <= L <= N)
# 시간복잡도: O(KN^2)
"""
mod = 1000000000
n, k = map(int, input().split())
d = [[0]*(n+1) for _ in range(k+1)]
d[0][0] = 1

for i in range(1, k+1):
    for j in range(0, n+1):
        for l in range(0, j+1):
            d[i][j] += d[i-1][j-l]
        d[i][j] %= mod

print(d[k][n])
