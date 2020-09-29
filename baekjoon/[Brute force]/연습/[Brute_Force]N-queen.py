# N 퀸 # B_9663
# 백트래킹 문제

"""
s[i][j]
대각선: i+j가 같은 애들끼리 짝지으면 대각선 도출 가능
반대 대각선: i-j가 같은 애들끼리
"""
def check(row, col):  # 퀸을 놓을 수 있는지 체크 / 못놓으면 버림->백트래킹
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+n-1]:
        return False
    return True

def calc(row):
    if row == n:
        return 1
    ans = 0
    for col in range(n):
        if check(row,col):
            check_dig[row+col] = True  # 대각선
            check_dig2[row-col+n-1] = True  #반대 대각선
            check_col[col] = True  # 열 체크
            a[row][col] = True  # 행 체크
            ans += calc(row+1)
            check_dig[row+col] = False
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            a[row][col] = False
    return ans

n = int(input())
a = [[False]*n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2*n-1)
check_dig2 = [False] * (2*n-1)
print(calc(0))

