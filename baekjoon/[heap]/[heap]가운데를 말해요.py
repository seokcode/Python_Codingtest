# 가운데를 말해요 # B_1655
import sys
import heapq


def solution(max_heap, min_heap, value):
    # max_heap의 루트 노드가 중간값
    # max_heap의 루트는 항상 min_heap의 루트보다 같거나 작아야 한다
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -value)
    else:
        heapq.heappush(min_heap, value)

    if min_heap and -max_heap[0] > min_heap[0]:
        temp_max = -heapq.heappop(min_heap)
        temp_min = -heapq.heappop(max_heap)

        heapq.heappush(max_heap, temp_max)
        heapq.heappush(min_heap, temp_min)


num = int(sys.stdin.readline())
max_heap, min_heap = [], []

for i in range(num):
    n = int(sys.stdin.readline())
    solution(max_heap,min_heap,n)

    print(-max_heap[0])
