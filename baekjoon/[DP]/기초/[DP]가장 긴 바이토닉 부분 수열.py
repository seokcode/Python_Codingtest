# 가장 긴 바이토닉 부분 수열 # B_11054
# 바이토닉: 한번 증가했다 한번 감소
# 각각의 수를 기준으로 가장 긴 증가하는 부분 수열(D)과 가장 긴 감소하는 부분 수열(D2)
# 를 구한 다음 D[i] + D2[i] -1 이 가장 큰 값을 찾으면 된다.

n = int(input())
a = list(map(int, input().split()))
d1 = [0]*n
d2 = [0]*n

for i in range(n):
    d1[i] = 1
    for j in range(i):
        if a[j] < a[i] and d1[i] < d1[j]+1:
            d1[i] = d1[j]+1

for i in range(n-1,-1,-1):
    d2[i] = 1
    for j in range(i+1,n):
        if a[i] > a[j] and d2[i] < d2[j]+1:
            d2[i] = d2[j]+1

d = [d1[i]+d2[i]-1 for i in range(n)]
print(max(d))