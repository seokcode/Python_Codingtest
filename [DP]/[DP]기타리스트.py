# 기타리스트 # B_1495
"""
0,1 Knapsack문제(가방 문제랑 비슷함)
# 볼륨을 올리거나 내리거나(2가지) = 2^n가지라서 많지만
# 가능한 볼륨의 범위가 0~m까지 이므로 m+1가지를 넘을 수 없음
D[i][j] = i번 곡을 볼륨 j로 연주할 수 있으면 1 없으면 0
자세한 풀이 교안참고(연습)
"""
n, s, m = map(int, input().split())  # 곡의 갯수, 시작볼륨, 최대 볼륨
v = [0]+list(map(int,input().split()))
d = [[-1]*(m+1) for _ in range(n+1)]
d[0][s] = 1
for i in range(n):
    for j in range(m+1):
        if d[i][j] == -1:
            continue
        if j-v[i+1] >= 0:
            d[i+1][j-v[i+1]] = 1

        if j+v[i+1] <= m:
            d[i+1][j+v[i+1]] = 1

# '마지막 곡을 연주할 수 있는 볼륨' 중 최댓값
ans = -1
for i in range(m + 1):
    if d[n][i] >= 0:
        ans = i

print(ans)
