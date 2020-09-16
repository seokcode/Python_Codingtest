# 점프 # B_1890
"""
# D[i][j] = (i,j)로 가는 경로의 개수
방법 1
D[i][j+A[i][j]] += D[i][j]
D[i+A[i][j]][j] += D[i][j]
# 시간복잡도: 두가지 중 하나(포문 안돔) O(1) * (i*j = N^2) = O(N^2)
"""
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0] = 1
for i in range(n):
    for j in range(n):
        if a[i][j] == 0:  # 0은 못가는 곳
            continue
        if j + a[i][j] < n:  # 인덱스가 0~ n-1까지 있음
            d[i][j+a[i][j]] += d[i][j]
        if i + a[i][j] < n:
            d[i+a[i][j]][j] += d[i][j]
print(d[n-1][n-1])
"""
# D[i][j] = (i,j)로 가는 경로의 개수
방법 2
2라고 쓰여진 칸을 밟았고 오른쪽으로 이동한다면
현재 밟고 있는 좌표 (i,k), 2칸 뒤 좌표(i,j)라고 했을 때 j-k = 2가 되어야 함
즉, 오른쪽으로 이동 시 j-k = A[i][k]

같은 방법으로 아래로 이동한다면
i-k = A[k][j]

시간복잡도: (i*j = N^2 )* 두 방법 중 하나 O(N) = O(N^3)

# 방법 2
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0] = 1
for i in range(n):
    for j in range(n):  # N^2
        if i == 0 and j == 0:
            continue
        for k in range(j):  # N
            if k + a[i][k] == j:
                d[i][j] += d[i][k]
        for k in range(i):  # N  => 총 N^3
            if k + a[k][j] == i:
                d[i][j] += d[k][j]
print(d[n-1][n-1])
"""