# 가장 긴 증가하는 부분 수열(LIS) 4 # B_11053
# 가장 긴 답 수열을 실제로 출력해야 함
# v[i]를 통해 자신의 앞에 오는 수의 인덱스를 저장하여 줄줄이 기차처럼 출력

n = int(input())
a = list(map(int, input().split()))
d = [0]*n
v = [-1]*n
for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[j]+1 > d[i]:
            d[i] = d[j]+1
            v[i] = j
ans = max(d)
p = [i for i, x in enumerate(d) if x == ans][0]
print(ans)

def go(p):
    if p == -1:
        return
    go(v[p])
    print(a[p], end=' ')

go(p)

