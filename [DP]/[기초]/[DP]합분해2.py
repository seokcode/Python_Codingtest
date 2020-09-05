# 합분해2 # B_13707
"""
# D[K][N] = 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
# 마지막 수: L
# 1에 비해 N,K의 범위가 매우 넓다
# 1과 같은 방법으로는 안되기때문에 다른 방법 사용
# 시간복잡도: O(KN) 으로 해결 가능
# pdf 그림 참조
"""
mod = 1000000000
n,k = map(int,input().split())
d = [[0]*(n+1) for _ in range(k+1)]
d[0][0] = 1
for i in range(1, k+1):
    for j in range(0, n+1):
        d[i][j] = d[i-1][j]
        if j-1 >= 0:
            d[i][j] += d[i][j-1]
        d[i][j] %= mod
print(d[k][n])

