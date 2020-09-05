# 1,2,3더하기 # B_9095
# D[n] = n을 나타내는 방법의 수
# D[n] = D[n-1]+D[n-2]+D[n-3]

d = [0]*11
d[0] = 1

d[1] = 1
d[2] = 2
for i in range(1, 10+1):
    if i >= 3:
        d[i] = d[i-1]+d[i-2]+d[i-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])
