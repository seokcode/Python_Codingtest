# 부분수의 합2 # B_1208
# 중간에서 만나기 / 교안참고
# N개가 있다고 할 때 M=2/N개 N-M개로 나누어 계산하여 시간복잡도를 줄임
"""
n:5 s:0
-7 -3 -2 5 8 일 때,
"""
n, s = map(int, input().split())
a = list(map(int, input().split()))
m = n//2
n = n-m

first = [0]*(1<<n)  # first: [-7,-3,-2]로 만들 수 있는 모든 부분 수열
for i in range(1<<n):
    for k in range(n):
        if (i&(1<<k)) > 0:
            first[i] += a[k]
# first = [0,-7,-3,-10,-2,-9,-5,-12]

second = [0]*(1<<m)  # second: [5, 8]로 만들 수 있는 모든 부분 수열
for i in range(1<<m):
    for k in range(m):
        if (i&(1<<k)) > 0:
            second[i] += a[k+n]
# second = [0,5,8,13]

first.sort()
second.sort()
second.reverse()


n = (1<<n)
m = (1<<m)
i, j, ans = 0, 0, 0

while i < n and j < m:
    if first[i] + second[j] == s:
        c1 = 1
        c2 = 1
        i += 1
        j += 1
        while i < n and first[i] == first[i-1]:
            c1 += 1
            i += 1
        while j < m and second[j] == second[j-1]:
            c2 += 1
            j += 1
        ans += c1*c2  # 어떤 짝이 답이 되었을 때 중복되는 짝이라면 추가
    elif first[i] + second[j] < s:
        i += 1
    else:
        j += 1
if s == 0:
    ans -= 1
print(ans)
