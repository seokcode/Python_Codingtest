"""
# 1,2,3 더하기 5 # B_15990
# 단, 같은 수를 두 번 이상 연속해서 사용하면 안된다.
# 점화식을 다음과 같이 수정
# D[i][j] = i를 1,2,3의 합으로 나타내는 방법의 수, 마지막에 사용한 수는 j
* D[i][1] = D[i-1][2] + D[i-1][3]
* D[i][2] = D[i-1][1] + D[i-1][3]
* D[i][3] = D[i-1][1] + D[i-1][2]
"""
limit = 100000
d = [[0]*4 for _ in range(limit+1)]
mod = 1000000009

for i in range(1, limit+1):
    if i-1 >= 0:
        d[i][1] = d[i-1][2] + d[i-1][3]
        if i == 1:
            d[i][1] = 1
    if i-2 >= 0:
        d[i][2] = d[i-2][1] + d[i-2][3]
        if i == 2:
            d[i][2] = 1
    if i-3 >= 0:
        d[i][3] = d[i-3][1] + d[i-3][2]
        if i == 3:
            d[i][3] = 1
    d[i][1] %= mod
    d[i][2] %= mod
    d[i][3] %= mod

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(d[n]) % mod)
