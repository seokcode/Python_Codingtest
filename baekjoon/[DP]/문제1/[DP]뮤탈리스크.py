# 뮤탈리스크 # B_12869
"""
D[a][b][c] = SCV의 체력이 i,j,k일 때, 모두 파괴하기 위해 공격해야 하는 횟수의 최솟값

공격 방법
1) 1,2,3: D[a-9][b-3][c-1]
2) 1,3,2: D[a-9][b-1][c-3]
3) 2,1,3: D[a-3][b-9][c-1]
4) 2,3,1: D[a-3][b-1][c-9]
5) 3,1,2: D[a-1][b-9][c-3]
6) 3,2,1: D[a-1][b-3][c-9]

tip) SCV가 최대 3개 있을 수 있기 때문에 1개, 2개일 경우를 따로 구하지 말고
그냥 3개라고 가정한 뒤 1개,2개일 경우는 이미 2개혹은 1개가 파괴된 것으로 생각하고 코딩
"""
n = int(input())
scv = list(map(int, input().split()))

while len(scv) < 3:  # tip
    scv += [0]

d = [[[-1]*61 for _ in range(61)] for _ in range(61)]


def go(a, b, c):
    if a < 0:
        return go(0, b, c)
    if b < 0:
        return go(a, 0, c)
    if c < 0:
        return go(a, b, 0)
    if a == 0 and b == 0 and c == 0:
        return 0
    ans = d[a][b][c]
    if ans != -1:
        return ans
    ans = 10000000

    if ans > go(a-1, b-3, c-9):
        ans = go(a-1, b-3, c-9)
    if ans > go(a-1, b-9, c-3):
        ans = go(a-1, b-9, c-3)
    if ans > go(a-3, b-9, c-1):
        ans = go(a-3, b-9, c-1)
    if ans > go(a-3, b-1, c-9):
        ans = go(a-3, b-1, c-9)
    if ans > go(a-9, b-3, c-1):
        ans = go(a-9, b-3, c-1)
    if ans > go(a-9, b-1, c-3):
        ans = go(a-9, b-1, c-3)
    ans += 1
    d[a][b][c] = ans
    return d[a][b][c]


print(go(scv[0], scv[1], scv[2]))
