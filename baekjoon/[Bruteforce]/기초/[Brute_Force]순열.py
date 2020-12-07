# 순열 # B_10972
# 1 ~ N 까지로 이루어진 순열
# 크기는 항상 N 이어야 하고, 겹치는 숫자가 존재하지 않음
# 크기가 N인 순열은 총 N!개가 존재한다
# N * N-1 * N-2 * N-3 * ... ==> N!

# 다음 순열
# 순열을 사전순으로 나열했을 때, 사전순으로 다음에 오는 순열과 이전에 오는 순열을 찾는 방법
# 첫 순열은 오름차순(1,2,3,4) 마지막 순열은 내림차순(4,3,2,1)
# 723의 마지막 순열: 7236541 -> 723 6>5>4>1(내림차순)
# 내림차순이 시작 되는 곳 6(i), 그 전 값 3(i-1)
# 그 다음에 오는 첫 순열은? 오른쪽에서 3보다 크면서 가장 작은 수 = 4(j)
# 7236541 -> 7246531 -> 724 1<3<5<6 (첫 순열은 오름차순)
# 1. i-1을 찾는거? O(N)
# 2. j를 찾는거? O(N)
# 3. 두 수를 바꾸는거 O(1)
# 4. 바꾼 뒤 순서를 뒤집는 거 O(N)
# 각각 독립된 단계이므로 총 시간 복잡도는 O(N)


def soonyeol(sy):

    i = N-1  # == len(sy) - 1
    while i > 0 and sy[i-1] >= sy[i]:
        i -= 1
    if i <= 0:
        return False

    j = N-1  # == len(sy) - 1
    while sy[j] <= sy[i-1]:
        j -= 1
    sy[i-1], sy[j] = sy[j], sy[i-1]  # swap

    j = N-1  # == len(sy) - 1
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

