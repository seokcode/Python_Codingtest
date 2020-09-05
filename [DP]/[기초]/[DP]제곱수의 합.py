# 제곱수의 합 # B_1699
# 1,2,3 더하기와 비슷
"""
# D[N] = min(D[N-i^2]) + 1 (단, 1 <= i^2 <= N)
# 시간복잡도: O(N*root.N)
"""
n = int(input())
d = [0]*(n+1)

for i in range(1,n+1):
    d[i] = i
    j = 1
    while j*j <= i:
        if d[i] > d[i-j*j] + 1:
            d[i] = d[i-j*j] + 1
        j += 1

print(d[n])
