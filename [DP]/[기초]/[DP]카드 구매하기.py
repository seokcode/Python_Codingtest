"""
# D[i] = 카드 i개를 구매하는 최대 비용
# 카드 1개가 들어있는 카드팩을 구매하고, 카드 i-1개를 구매: P[1] + D[i-1]...P[i-1] + D[1]
# 카드 i개를 구매하는 방법은? 카드 j개가 들어있는 카드팩을 구매하고 카드 i-j개를 구매
# D[i] = max(P[j] + D[i-j]) (1 <= j <= i)
# 시간복잡도: O(N^2)
"""
# 카드 구매하기 # B_11052

n = int(input())
a = [0] + list(map(int, input().split()))
d = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j]+a[j])

print(d[n])