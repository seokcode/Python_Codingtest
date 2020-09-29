# 큐 2 # B_18258
import sys
from collections import deque
input = sys.stdin.readline

q = deque([])
n = int(input())
for i in range(n):
    order=input().split()
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        if not q:
            print(-1)
            # 큐가 비어있다면
        else:
            print(q.popleft())
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif order[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])