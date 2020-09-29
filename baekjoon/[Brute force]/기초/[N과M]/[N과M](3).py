# N과M 3 # B_15651
# (1)과 같지만 같은 수를 여러번 골라도 됨 -> (2,2) 가능
import sys
n, m = map(int, input().split())
a = [0]*m  # 정답을 넣는 배열


def nm(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(1, n+1):
        # 중복 불가. 즉, 해당 수를 사용했다면 넘어가야함
        a[index] = i
        nm(index+1, n, m)  # 다음 위치 찾기

nm(0, n, m)
