# 이동하기 # B_11048
"""
# D[i][j] = (1,1) 시작 (i,j)도착 합의 최대값
# (i,j)를 오는 경로가
    1. 윗 칸에서 온 경우
    최대값: D[i-1][j]+A[i][j]
    2. 왼 대각선 윗 칸에서 온 경우
    최대값: D[i-1][j-1]+A[i][j]
    3. 옆 칸에서 온 경우
    최대값: D[i][j-1]+A[i][j]
so, D[i][j] = max(D[i-1][j], D[i-1][j-1], D[i][j-1]) + A[i][j]

**** 본 문제에서는 A[i][j] >= 0 이 항상 성립하여 [i-1][j],[i-1][j-1],[i][j-1]
의 범위 검사를 하지 않았지만 만약 A[i][j] 이 음수가 가능했다면 범위 검사를 해줘야 함
"""

n, m = map(int, input().split())
A = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
D = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        D[i][j] = max(D[i - 1][j], D[i - 1][j - 1], D[i][j - 1]) + A[i][j]

print(D[n][m])

# 방법2, 3, 4까지 존재함
