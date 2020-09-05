# N과M 2 # B_15650
# 오름차순 조건 추가 # 무슨 말이야? (1,2) (2,1) 같은 거란 말

# 방법 1
import sys
n, m = map(int, input().split())
# 오름차순이므로 중복 될 일이 없어서 제거
# check = [False]*(n+1)
a = [0]*m  # 정답을 넣는 배열


def nm2(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return

    for i in range(start, n+1):
        a[index] = i
        nm2(index+1, i+1, n, m)

nm2(0, 1, n, m)


# 방법 2 (수를 사용한다, 안한다로 나누어서 풀이)
# 더 대중적인 알고리즘
def nm2_2(index, selected, n, m):
    # selected: 총 몇개를 골랐는가?
    if selected == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return

    if index > n:
        return

    a[selected] = index
    nm2_2(index+1, selected+1, n, m)  # 해당 숫자를 선택하는 경우
    a[selected] = 0  # 선택 초기화
    nm2_2(index+1, selected, n, m)  # 선택 안하는 경우


nm2_2(1, 0, n, m)
