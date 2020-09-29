# 연속합 2 # B_1912
"""
# 연속합을 구하고 수 하나를 제거 할 수 있음 그때의 최댓값
# dl[i] = 왼쪽에서부터 구한 연속합 정답
# dr[i] = 오른쪽에서부터 구한 연속합 정답
# 각각의 제거할 수 k에 대해서 dl[k-1]+dr[k+1]의 최대값이 정답이 된다
"""
n = int(input())
a = list(map(int, input().split()))
d = [0]*n
dr = [0]*n
for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if d[i] < d[i-1] + a[i]:
        d[i] = d[i-1] + a[i]

for i in range(n-1,-1,-1):
    dr[i] = a[i]
    if i == n-1:
        continue
    if dr[i] < dr[i+1] + a[i]:
        dr[i] = dr[i+1] + a[i]

ans = max(d)
for i in range(1, n-1):
    if ans < d[i-1] + dr[i+1]:
        ans = d[i-1] + dr[i+1]

print(ans)