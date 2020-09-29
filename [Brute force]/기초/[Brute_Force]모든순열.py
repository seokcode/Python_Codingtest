# 모든 순열 # B_10974
# 다음 순열이 없을때까지 하면 됨
# 순열의 모든 순서 : N!
# 그렇다면 모든 순열을 구하는 시간 복잡도?: 다음순열 * N! => O(N*N!)
# 1억개를 계산할때 1초가 걸리므로 본 알고리즘은 N이 10이하일 경우에만 시간 내 가능
def soonyeol(sy):

    i = len(sy) - 1
    while i > 0 and sy[i-1] >= sy[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(sy) - 1
    while sy[j] <= sy[i-1]:
        j -= 1
    sy[i-1], sy[j] = sy[j], sy[i-1]  # swap

    j = len(sy) - 1
    while i < j:
        sy[i], sy[j] = sy[j], sy[i]  # swap
        i += 1
        j -= 1

    return True


N = int(input())
sy = list(range(1, N+1))
# == # for i in range(1, N+1):
# #      sy.append(i)

while True:
    print(' '.join(map(str, sy)))
    if not soonyeol(sy):
        break
