# 참고 #
# 순열은 1,1,2,2,2와 같이 같은 수가 있어도 잘 수행이 됨
# 이 때 경우의 수? 5!/ 2! * 3!
# (전체 경우의 수)/ (같은 수 1의 경우의 수) * (같은 수 1의 경우의 수)

# 로또 # B_6603
# 고르는 문제도 순열로 바꾸어 풀이 가능
# 이 때, 고르는 갯수가 변하면 안됨 일정해야함
# ex) 6개를 고르세요(O) 6개,5개,4개를 고르세요(X)


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


while True:
    # 첫 번째 인덱스와 나머지 인덱스 분리하여 저장
    N, *a = list(map(int, input().split()))
    if N == 0:
        break

    num = [0] * (N-6) + [1] * 6  # 첫 순열 오름차순
    ans = []
    while True:
        # num[i] == 1 일때 a[i]의 값을 temp 리스트 인덱스에 추가(N만큼 반복)
        temp = [a[i] for i in range(N) if num[i] == 1]
        ans.append(temp)
        if not soonyeol(num):
            break

    ans.sort()
    for j in ans:
        print(' '.join(map(str, j)))
    print()





