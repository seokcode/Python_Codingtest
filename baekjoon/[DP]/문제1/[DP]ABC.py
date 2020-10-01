# ABC # B_12969
"""
D[i][a][b][p] = 길이가 i이고, A의 개수가 a개, B의 개수가 b개, S[i]<S[j] 쌍이 p개 있는
문자열이 가능한가?

1. i번째 글자가 A인 경우: D[i+1][a+1][b][p]
2. i번째 글자가 B인 경우(이 때, 쌍의 갯수는 a의 갯수만큼 더 늘어남): D[i+1][a][b+1][p+a]
3. i번째 글자가 C인 경우(이 때, 쌍의 갯수는 a,b의 갯수만큼 더 늘어남): D[i+1][a][b+1][p+a+b]
"""
d = [[[[False]*436 for _ in range(31)] for _ in range(31)] for _ in range(31)]
n, k = map(int, input().split())
ans = ''


# go의 return값과 d의 T/F값 혼동 주의
def go(i, a, b, p):
    if i == n:
        if p == k:
            return True
        else:
            return False

    if d[i][a][b][p]:
        return False

    d[i][a][b][p] = True  # 한번 했음을 체크
    global ans
    temp = ans
    ans = temp + 'A'
    if go(i+1, a+1, b, p):
        return True
    ans = temp + 'B'
    if go(i+1, a, b+1, p+a):
        return True
    ans = temp + 'C'
    if go(i+1, a, b, p+a+b):
        return True

    return False


if go(0, 0, 0, 0):
    print(''.join(ans))
else:
    print(-1)
