# 차이를 최대로 # B_10819
# 3<= N <=8 이므로 브루트포스로 1초 안에 가능
# O(N*N!) = O(8*8!)


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


def caculate(sy):
    s = 0
    for i in range(len(sy)-1):
        s += abs(sy[i]-sy[i+1])
    return s


N = int(input())
sy = list(map(int, input().split()))
sy.sort()  # 첫 순열은 오름차순
ans = 0

while True:
    temp = caculate(sy)
    ans = max(ans, temp)

    if not soonyeol(sy):
        break

print(ans)
