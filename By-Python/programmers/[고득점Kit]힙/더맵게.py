# 더 맵게
import heapq


def solution(scoville, K):
    answer, rate = 0, 0
    heapq.heapify(scoville)

    while scoville:
        hot1 = heapq.heappop(scoville)
        if hot1 >= K:
            return answer
        if scoville:
            hot2 = heapq.heappop(scoville)
            rate = hot1 + (hot2 * 2)
            heapq.heappush(scoville, rate)
            answer += 1

    return -1