# deque #  10866
import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
deq = deque([])
count = 0
for i in range(num):
    order=input().split()
    if order[0] == "push_back":
        deq.append(int(order[1]))
        count+=1
    elif order[0] == "push_front":
        deq.appendleft(int(order[1]))
        count+=1
    elif order[0] == "front":
        if count==0:
            print(-1)
        else:
            print(deq[0])
    elif order[0] == "back":
        if count==0:
            print(-1)
        else:
            print(deq[-1])
    elif order[0] == "size":
        print(count)
    elif order[0] == "empty":
        if count==0:
            print(1)
        else:
            print(0)
    elif order[0] == "pop_front":
        if count == 0:
            print(-1)
        else:
            print(deq.popleft())
            count -= 1
    elif order[0] == "pop_back":
        if count == 0:
            print(-1)
        else:
            print(deq.pop())
            count -= 1