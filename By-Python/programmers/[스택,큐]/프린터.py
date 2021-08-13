# 프린터

from collections import deque

def solution(priorities, location):
    answer = 0
    deq = deque([(n, idx) for idx, n in enumerate(priorities)])

    while len(deq):
        compare = deq.popleft()
        if deq and max(deq)[0] > compare[0]:
            deq.append(compare)
        else:
            answer += 1
            if compare[1] == location:
                break

    return answer