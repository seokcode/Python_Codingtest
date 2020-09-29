# 최소 힙 # B_1927
import sys
import heapq

n = int(input())
heap = []
count = 0
for _ in range(n):
    num = int(sys.stdin.readline())

    if num != 0:
        heapq.heappush(heap, (-num))
        count += 1
    else:
        if count != 0:
            print(-1 * heapq.heappop(heap))
            count -= 1
        else:
            print(0)