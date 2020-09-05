# 연속합 # B_1912
# 시간 복잡도 O(N)
# D[i] = A[i]에서 끝나는, 연속 값의 최댓값
# D[i] = max(A[i], D[i-1]+A[i])

n = int(input())
a = list(map(int, input().split()))
d = [0]*n

for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if d[i] < d[i-1] + a[i]:
        d[i] = d[i-1] + a[i]

print(max(d))
