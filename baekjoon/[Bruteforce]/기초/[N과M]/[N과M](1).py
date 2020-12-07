# N과M # B_15649
import sys
n, m = map(int, input().split())
check = [False]*(n+1)
a = [0]*m  # 정답을 넣는 배열


def nm(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(1, n+1):
        # 중복 불가. 즉, 해당 수를 사용했다면 넘어가야함
        if check[i]:
            continue
        check[i] = True  # 사용했으면 True
        a[index] = i
        nm(index+1, n, m)  # 다음 위치 찾기
        check[i] = False  # 한 패턴을 돌고 나면 초기


nm(0, n, m)