# 파일합치기 # B_11066
"""
# 연속된 파일만 합칠 수 있다.
# d[i][j] = i번~ j번까지를 합치는 최소 비용
# 예를 들어 파일 다섯개 1,2,3,4,5 가 있다고 하면 파일을 합치는 방법은
# * @ @ @ @ : (1~1)/(2~5) -> (1~5) : d[1][1] + d[2][5] + 1~5파일크기
# * * @ @ @ : (1~2)/(3~5) -> (1~5) : d[1][2] + d[3][5] + 1~5파일크기
# * * * @ @ : (1~3)/(4~5) -> (1~5) : d[1][3] + d[4][5] + 1~5파일크기
# * * * * @ : (1~4)/(5~5) -> (1~5) : d[1][4] + d[5][5] + 1~5파일크기
so, i~j까지 파일이 있다고 하면 파일을 합치는 방법은(k에서 나눠진다고할 때)
d[i][k] + d[k+1][j] + i~j번째 파일 크기의 합 (i<=k<=j-1)
"""
import sys

def go(i, j):
    if i == j:
        return 0
    # 한번 돌 때 d[i][j]의 최솟값을 구해서 한번에 넣기때문에
    # -1 이면 이미 작업이 끝난 상태를 의미
    if d[i][j] != -1:
        return d[i][j]
    ans = d[i][j]
    cost = sum(file[i:j+1])
    for k in range(i, j):
        temp = go(i,k) + go(k+1,j) + cost
        if ans == -1 or ans > temp:
            ans = temp
    d[i][j] = ans
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    file = list(map(int, sys.stdin.readline().split()))
    d = [[-1]*n for _ in range(n)]
    print(go(0, n-1))