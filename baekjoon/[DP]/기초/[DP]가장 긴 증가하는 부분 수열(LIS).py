# 가장 긴 증가하는 부분 수열(LIS) # B_11053
# 시간 복잡도: O(N^2)
# a[j] < a[i] and D[i] < D[j]+1 을 만족하는 모든 j에 대해서
# D[i] = max(D[j]) + 1

n = int(input())
a = list(map(int, input().split()))
d = [0]*n

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j]+1:
            d[i] = d[j] + 1

print(max(d))