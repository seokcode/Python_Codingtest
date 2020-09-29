# 카드2 # B_2164
import sys
from collections import deque
input = sys.stdin.readline

q = deque([])
n = int(input())
count=0
for i in range(1, n+1):
    q.append(i)
    count+=1

while count!=1:
    q.popleft()
    q.rotate(-1)
    count-=1

for i in q:
    print(i)