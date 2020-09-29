# 이전 순열 # B_10973
# 다음 순열에서 부등호만 바뀌면 됨

def soonyeol(sy):

    i = len(sy) - 1
    while i > 0 and sy[i-1] <= sy[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(sy) - 1
    while sy[j] >= sy[i-1]:
        j -= 1
    sy[i-1], sy[j] = sy[j], sy[i-1]  # swap

    j = len(sy) - 1
    while i < j:
        sy[i], sy[j] = sy[j], sy[i]  # swap
        i += 1
        j -= 1

    return True


N = int(input())
sy = list(map(int, input().split()))

if soonyeol(sy):
    print(' '.join(map(str,sy)))
else:
    print(-1)