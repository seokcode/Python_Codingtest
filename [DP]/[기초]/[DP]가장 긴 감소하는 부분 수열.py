# 가장 긴 감소하는 부분 수열 # B_11722
# 방법 2가지

n = int(input())
a = list(map(int, input().split()))
d = [0]*n
for i in range(n-1,-1,-1):
    d[i] = 1
    for j in range(i+1,n):
        if a[i] > a[j] and d[i] < d[j]+1:
            d[i] = d[j]+1

print(max(d))