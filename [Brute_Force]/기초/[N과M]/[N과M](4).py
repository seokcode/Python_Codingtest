# N과M 4 # B_15652
# (2)와 같지만 같은 수 여러번 선택 가능 & 비내림차순(같은 것도 허용하는 오름차순)

# 방법 1
import sys
n, m = map(int, input().split())
a = [0]*m  # 정답을 넣는 배열


def nm4_1(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return

    for i in range(start, n+1):
        a[index] = i
        nm4_1(index+1, i, n, m)  # i+1: 중복허용x -> i: 중복허용o


nm4_1(0, 1, n, m)


# **방법 2**
# 선택하는 경우/ 안하는 경우로 나누는건 동일하나 중복이 허용됨으로
# 몇개를 선택할건지 조건에 추가해야 함
cnt = [0]*(n+1)  # i를 몇 개 선택했는지?


def nm4_2(index, selected, n, m):
    # selected: 총 몇개를 골랐는가?
    if selected == m:
        for i in range(1, n+1):
            for j in range(cnt[i]):
                sys.stdout.write(str(i)+' ')
        sys.stdout.write('\n')
        return

    if index > n:
        return

    # 큰 자릿 수 부터 계산하는 이유? -> 사전순 출력이므로
    # 111 이 112 보다 앞섬 즉 적은 수가 많은것이 자릿수가 동일한 경우 앞섬
    for i in range(m-selected, 0, -1):  # 고른 경우
        cnt[index] = i
        nm4_2(index+1, selected+i, n, m)

    cnt[index] = 0  # 안고른 경우
    nm4_2(index+1, selected, n, m)


nm4_2(1, 0, n, m)
