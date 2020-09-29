# 외판원 순회2 # B_10971
# 한 도시에서 시작해 N개의 모든 도시를 거쳐 다시 원래 도시로 돌아오려고 한다.
# 한번 갔던 도시로는 다시 갈 수 없다 -> 순열
# 여기서 N의 조건이 중요 10이하면 순열로 가능


# 방법 1 / 시간 복잡도: O(N*N!)
def soonyeol(sy):

    i = N-1
    while i > 0 and sy[i-1] >= sy[i]:
        i -= 1
    if i <= 0:
        return False

    j = N-1
    while sy[j] <= sy[i-1]:
        j -= 1
    sy[i-1], sy[j] = sy[j], sy[i-1]  # swap

    j = N-1
    while i < j:
        sy[i], sy[j] = sy[j], sy[i]  # swap
        i += 1
        j -= 1

    return True


N = int(input())
w = [list(map(int, input().split())) for _ in range(N)]
d = list(range(N))
ans = 2147483647  # 메르센 소수

while True:
    status = True
    s = 0
    for i in range(0, N-1):
        # N = 4이므로 방문하는 도시 0,1,2,3
        # (0,1) (1,2) (2,3)
        if w[d[i]][d[i+1]] == 0:
            status = False
            break
        else:
            s += w[d[i]][d[i+1]]

    # w[d[-1]][d[0]] = w[3][0]
    # => (0,1) (1,2) (2,3) -> (3,0),원래 도시로 복귀
    if status and w[d[-1]][d[0]] != 0:
        s += w[d[-1]][d[0]]
        ans = min(ans, s)
    if not soonyeol(d):
        break
    # 방법 2. 아래 두줄 추가 -> 시간복잡도: O(N!)
    # 왜? -> 0123 1230 2301 3012 전부 같은 경우이므로 시작점을 0으로 고정해도 무관하다
    if d[0] != 0:
        break

print(ans)