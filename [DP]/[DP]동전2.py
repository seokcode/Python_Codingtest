# 동전2 # B_2294
# 동전의 최소 갯수를 구하는 문제

n, k = map(int, input().split())
d = [-1] * (k+1)
d[0] = 0
value = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(1, k+1):
        if j - value[i] >= 0 and d[j-value[i]] != -1:
            if d[j] == -1 or d[j] > d[j-value[i]] + 1:
                d[j] = d[j-value[i]] + 1


print(d[k])
