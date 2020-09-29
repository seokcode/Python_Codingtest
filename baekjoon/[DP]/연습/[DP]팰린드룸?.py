# 팰린드롬? # B_10942
# 팰린드롬: 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열
# 팰린드롬인지 확인하는데 걸리는 시간: O(N) / 문자열 길이: N
# 질문이 M개면 O(MN)이라는 시간이 걸림 -> 문제의 범위를 보면 이 방법으로는 불가능
"""
D[i][j] = A[i]~A[j]까지가 팰린드롬이면 1 아니면 0
길이가 1인 문자열: 항상 참
길이가 2인 문자열: A[i]=A[i+1]인 경우에만 참
길이가 3 이상: A[i] = A[j]이며 D[i+1][j-1] = 팰린드
"""
# bottom-up
import sys
n = int(input())
a = list(map(int,sys.stdin.readline().split()))
d = [[False]*n for _ in range(n)]

for i in range(n):  # 길이 1일때
    d[i][i] = True
for i in range(n-1):  # 길이 2일때
    if a[i] == a[i+1]:
        d[i][i+1] = True
for k in range(3, n+1):  # 길이 3 이상
    for i in range(1, n-k+1):
        j = i+k-1
        if a[i] == a[j] and d[i+1][j-1]:
            d[i][j] = True


tc = int(sys.stdin.readline())
for _ in range(tc):
    s, e = map(int, sys.stdin.readline().split())
    print(1 if d[s][e] else 0)

# top-down
"""
import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d = [[-1]*n for _ in range(n)]
def go(i, j):
    if i == j:
        return 1
    elif i+1 == j:
        if a[i] == a[j]:
            return 1
        else:
            return 0
    if d[i][j] != -1:
        return d[i][j]
    if a[i] != a[j]:
        d[i][j] = 0
    else:
        d[i][j] = go(i+1,j-1)
    return d[i][j]
m = int(sys.stdin.readline())
for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    print(go(s-1,e-1))
"""