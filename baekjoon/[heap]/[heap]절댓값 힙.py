# 절댓값 힙 # B_11286
import sys
import heapq

n = int(sys.stdin.readline())
heap = []
count = 0
for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
        count += 1
    else:
        if count != 0:
            print(heapq.heappop(heap)[1])
            count -= 1
        else:
            print(0)
