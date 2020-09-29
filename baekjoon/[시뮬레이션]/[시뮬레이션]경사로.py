# 경사로 # B_14890

"""
------->
|
|
V
"""
def go(a, l):
    n = len(a)
    c = [False] * n
    for i in range(1, n):  # 길이만큼 반복(행 길이=열 길이)
        if a[i-1] != a[i]:  # 이웃한 블럭의 높이가 같지 않다면
            diff = abs(a[i]-a[i-1])  # 차이를 구하고
            if diff != 1:  # 차이가 1이 아니라면 나가리
                return False
            if a[i-1] < a[i]:  # 차이가 1인데 오른쪽,아랫쪽이 더 큰 경우
                for j in range(1, l+1):  # 경사로의 길이까지 반복
                    if i-j < 0:
                        # 경사로를 놓다가 범위를 벗어나는 경우
                        # i는 인덱스 번호이므로 왼쪽부터 얼마나 떨어져있는지를 의미
                        return False
                    if a[i-1] != a[i-j]:
                        # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                        return False
                    if c[i-j]:
                        # 경사로를 놓은 곳에 또 경사로를 놓는 경우
                        return False
                    c[i-j] = True
            else:  # 차이가 1인데 왼쪽,위쪽이 더 큰 경우
                for j in range(l):
                    if i+j >= n:
                        # 길이가 0~n-1 이고 왼쪽에서 i만큼 떨어져 있는 블럭의 오른쪽에
                        # 경사로를 놓기 때문에 i+경사로길이(l) >= n이면 초과
                        return False
                    if a[i] != a[i+j]:
                        return False
                    if c[i+j]:
                        return False
                    c[i+j] = True
    return True


n, l = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
"""
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2 일 떄,
a[0] = [3,3,3,3,3,3]
a[1] = [2,3,3,3,3,3]
"""
for i in range(n):
    d = a[i]
    if go(d, l):  # 한 행 검사
        ans += 1  # 경로가 있다면 +1
for j in range(n):
    d = [a[i][j] for i in range(n)]  # 한 열 검사
    if go(d, l):
        ans += 1
print(ans)

