# circular queue # B_1021
import sys
from collections import deque
input = sys.stdin.readline

cir_q = deque([])
num, pick_n = map(int, input().split())
count = 0
for i in range(1, num+1):
    cir_q.append(i)
    count += 1

number = list(map(int, input().split()))
result = 0
for i in range(pick_n):
    temp = 0
    if number[i] == cir_q[0]:
        cir_q.popleft()
        count -= 1
    else:
        for j in range(count):
            if number[i] == cir_q[j]:
                temp = j
        if temp < (count / 2):
            while cir_q[0] != number[i]:
                cir_q.rotate(-1)
                result += 1
            cir_q.popleft()
            count -= 1
        elif temp >= (count / 2):
            while cir_q[0] != number[i]:
                cir_q.rotate(1)
                result += 1
            cir_q.popleft()
            count -= 1

print(result)