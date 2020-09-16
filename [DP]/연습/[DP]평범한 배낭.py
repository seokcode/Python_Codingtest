# 평범한 배낭 # B_12865
# Knapsack 문제(유명한 알고리즘)
"""
물건을 가방에 넣은 경우/넣지 않은 경우(2가지)^물품의 최대 수 범위 100 = 2^100
2^100이기 떄문에 다 해볼 순 없음

d[n] = i번째 물건까지 고려했고, 배낭에 넣은 물건 무게의 합이 j일 때, 가치의 최댓값
so, i번째 물건을 가방에 넣지 않은 경우: D[i-1][j] (그 물건만 안넣으면 됨)
and, 넣은 경우: D[i-1][j+무게[i]] + 가치[i]
-> 그 물건은 넣었으니 -1 하고, 넣었으니 들고있는 무게에 그 물건의 무게를 더해줌 그리고 가치도 더해줌

# 1차원으로도 구현할 수 있다. 이때는 배열을 뒤에서부터 채워줘야함
앞에서부터 하면 같은 물건을 계속 사용하기 때문

import sys


n, k = map(int,sys.stdin.readline().split())
temp = [list(map(int,input().split())) for _ in range(n)]
w, v = zip(*temp)
w = [0] + list(w)
v = [0] + list(v)
d = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        d[i][j] = d[i-1][j]  # 물건을 가방에 안넣고 그냥 넘김
        if j-w[i] >= 0:  # 가방에 넣을 수 있다면 넣는것과 안넣는것을 비교
            d[i][j] = max(d[i][j], d[i-1][j-w[i]]+v[i]])

print(d[n][k])
"""
# 1차원으로도 구현할 수 있다
# 왜 뒤에서부터 채워야하는지 직접 해보기
n,k = map(int,input().split())
temp = [list(map(int,input().split())) for _ in range(n)]
w,v = zip(*temp)
w = [0] + list(w)
v = [0] + list(v)
d = [0]*(k+1)
for i in range(1, n+1):
    for j in range(k, 0, -1):
        if j-w[i] >= 0:  # 해당 물건을 넣었을 때 가방에 여유 공간이 있다면
            d[j] = max(d[j], d[j-w[i]]+v[i])
            # 가방에 넣되, 넣는것과 안넣는것 중 큰 가치를 갖는 값을 넣음
            # 단일 배열을 사용하는 경우
            # j의 범위를 1부터 k까지 하게 되면 같은 물건을 두번 사용하는 경우가 발생하므로
            # j를 k부터 역순으로 계산
print(d[k])

