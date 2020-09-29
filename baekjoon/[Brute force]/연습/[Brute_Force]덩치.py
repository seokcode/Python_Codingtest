# 덩치 # B_7568

n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x,y))

for i in xy:
    cnt = 1
    for j in xy:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=" ")
