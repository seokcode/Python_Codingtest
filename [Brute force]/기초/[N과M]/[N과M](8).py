# N과M 8 # B_15657
# (4)와 대응 # 중복허용 비내림차순


import sys
n, m = map(int, input().split())
num = list(map(int, input().split())) # [(1)과 다른 부분]
num.sort()  # 사전 순 정렬[(1)과 다른 부분]

# 방법 1
a = [0]*m  # 정답을 넣는 배열


def nm8(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(start, n):
        # 중복 불가. 즉, 해당 수를 사용했다면 넘어가야함
        a[index] = num[i]  # 입력으로 받은 수 최소 순으로 넣기[(1)과 다른 부분]
        nm8(index+1, i, n, m)  # 다음 위치 찾기


nm8(0, 0, n, m)


# 방법 2
cnt = [0]*n  # i를 몇 개 선택했는지?


def nm8_2(index, selected, n, m):
    # selected: 총 몇개를 골랐는가?
    if selected == m:
        for i in range(n):
            for j in range(cnt[i]):
                sys.stdout.write(str(num[i])+' ')
        sys.stdout.write('\n')
        return

    if index >= n:
        return

    # 큰 자릿 수 부터 계산하는 이유? -> 사전순 출력이므로
    # 111 이 11x 보다 앞섬 즉 적은 수가 많은것이 자릿수가 동일한 경우 앞섬
    for i in range(m-selected, 0, -1):  # 고른 경우
        cnt[index] = i
        nm8_2(index+1, selected+i, n, m)

    cnt[index] = 0  # 안고른 경우
    nm8_2(index+1, selected, n, m)


nm8_2(0, 0, n, m)
