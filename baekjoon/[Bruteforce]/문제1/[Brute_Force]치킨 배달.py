# 치킨 배달 # B_15686
"""
치킨 집 최대 13개 중에서 M개를 고르는 문제 == 링크와스타트
고른다, 안고른다 2가지 이므로 2^13 가지 = 8192가지 -> Brute_Force
"""
# 재귀함수 사
import sys
sys.setrecursionlimit(100000)

def go(index, cur_num):
    global ans
    if index > len(chicken):
        return
    if cur_num == m:  # 폐점하지 시키지 않을 치킨집을 다 고른 경우
        s = 0
        # 집에서의 각 치킨집 별로 치킨거리를 구함
        for px,py in house:
            dists = []
            for i,(cx,cy) in enumerate(chicken):
                if d[i]:
                    d1 = abs(px-cx)
                    d2 = abs(py-cy)
                    dists.append(d1+d2)
            # 집에서 가장 가까운 치킨거리를 구하여 도시의 치킨거리 구함
            dists.sort()
            s += dists[0]

        # 도시의 치킨 거리의 최솟값을 ans에 저장
        ans = min(ans,s)
        return

    # 폐점 시키지 않을 치킨집의 경우의 수 DFS
    d[index] = True
    go(index+1, cur_num+1)
    d[index] = False
    go(index+1, cur_num)


MAX_N = 1000000000
n, m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            house.append((i, j))
        elif a[i][j] == 2:
            chicken.append((i, j))

d = [False]*(len(chicken)+1)
ans = MAX_N
go(0, 0)
print(ans)

"""
# 순열 사용
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
people = []
store = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            people.append((i,j))
        elif a[i][j] == 2:
            store.append((i,j))
d = [0]*len(store)
for i in range(m):
    d[i] = 1
d.sort()
ans = -1
while True:
    s = 0
    for px,py in people:
        dists = []
        for i,(sx,sy) in enumerate(store):
            if d[i] == 0:
                continue
            d1 = abs(px-sx)
            d2 = abs(py-sy)
            dists.append(d1+d2)
        dists.sort()
        s += dists[0]
    if ans == -1 or ans > s:
        ans = s
    if not next_permutation(d):
        break
print(ans)
"""
