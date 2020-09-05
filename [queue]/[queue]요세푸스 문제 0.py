# 요세푸스 문제 0 # B_11866
import sys
from collections import deque
input = sys.stdin.readline

q = deque([])
result = []
num, d_num = map(int, input().split())
count = 0
s_num = 2
for i in range(1, num+1):
    q.append(i)
    count += 1
while count != 0:
    q.rotate(-(d_num-1))
    result.append(q.popleft())
    count -= 1

print("<", end="")
for i in range(num):
    if i==num-1:
        print(result[i], end=">")
    else:
        print(result[i], end=", ")



