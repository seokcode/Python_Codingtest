# 출근기록 # B_14238
"""
D[a][b][c][p1][p2] = A,B,C의 개수가 a,b,c이고, 전날 일한 사람이 p1, 그 전날 일한 사람이
p2인 것이 가능한가?

1. 오늘 일한 사람이 A인 경우: D[a+1][b][c]['A'][p1]
2. 오늘 일한 사람이 B인 경우: D[a][b+1][c]['B'][p1]
    2-1(조건). D[a][b][c][p1][p2]에서 p1 != 'B' 이어야 함
3. 오늘 일한 사람이 C인 경우: D[a][b][c+1]['C'][p1]
    3-1(조건). D[a][b][c][p1][p2]에서 p1,p2 != 'C','C' 이어야 함
"""

s = input()
limit = [0, 0, 0]
for ch in s:  # A=65, B=66, C=67
    limit[ord(ch)-ord('A')] += 1
    # limit[0] = 1, limit[1] = 2, limit[2] = 2

n = len(s)
d = [[[[[-1]*3 for _ in range(3)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]


def go(a, b, c, p1, p2):
    ans = d[a][b][c][p1][p2]
    if a+b+c == 0:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]

    if ans != -1:
        return ans

    if a > 0 and go(a-1, b, c, 0, p1) == 1:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    if b > 0 and p1 != 1 and go(a, b-1, c, 1, p1) == 1:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    if c > 0 and p1 != 2 and p2 != 2 and go(a, b, c-1, 2, p1) == 1:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]

    d[a][b][c][p1][p2] = 0
    return d[a][b][c][p1][p2]

def back(a,b,c,p1,p2):
    if a+b+c == 0:
        return ''
    if a > 0 and go(a - 1, b, c, 0, p1) == 1:
        return 'A' + back(a-1, b, c, 0, p1)

    if b > 0 and p1 != 1 and go(a, b - 1, c, 1, p1) == 1:
        return 'B' + back(a, b-1, c, 1, p1)

    if c > 0 and p1 != 2 and p2 != 2 and go(a, b, c - 1, 2, p1) == 1:
        return 'C' + back(a, b, c-1, 2, p1)
    return ''

ans = go(limit[0], limit[1], limit[2], 0, 0)
if ans == 0:
    print(-1)
else:
    print(back(limit[0], limit[1], limit[2], 0, 0))