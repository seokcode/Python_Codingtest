# 동전1 # B_2293
n, k = map(int, input().split())
d = [0] * (k+1)
d[0] = 1
value = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(1, k+1):
        if j - value[i] >= 0:
            d[j] += d[j-value[i]]


print(d[k])
