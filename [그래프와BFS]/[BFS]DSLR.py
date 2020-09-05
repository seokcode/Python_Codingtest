# DSLR # B_9019

from collections import deque
import sys
MAX = 10001  # 0~10000
sys.setrecursionlimit(MAX)

# 테스트 케이스의 최소한의 명령어 집합을 나열하는 함수
def way(n, m):
    if n == m:
        return
    way(n, via[m])
    print(how[m], end='')


t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, input().split())
    check = [False] * MAX
    dist = [-1] * MAX
    via = [-1] * MAX
    how = [''] * MAX
    check[n] = True
    dist[n] = 0
    q = deque()
    q.append(n)

    while q:
        now = q.popleft()
        # D연산
        next = (now*2) % 10000
        if not check[next]:
            q.append(next)
            check[next] = True
            dist[next] = dist[now] + 1
            via[next] = now
            how[next] = 'D'

        # S연산
        next = now-1
        if next == -1:
            next = 9999
        if not check[next]:
            q.append(next)
            check[next] = True
            dist[next] = dist[now] + 1
            via[next] = now
            how[next] = 'S'

        # L연산(왼편으로 회전) # 1234 -> 2341
        next = (now%1000)*10 + now//1000
        if not check[next]:
            q.append(next)
            check[next] = True
            dist[next] = dist[now] + 1
            via[next] = now
            how[next] = 'L'

        # R연산(오른편으로 회전) # 1234 -> 4321
        next = (now//10) + (now%10)*1000
        if not check[next]:
            q.append(next)
            check[next] = True
            dist[next] = dist[now] + 1
            via[next] = now
            how[next] = 'R'

    way(n, m)
    print()
