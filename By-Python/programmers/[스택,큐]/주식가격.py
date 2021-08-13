# 주식가격

# 정확성 통과, 효율성 불통
from collections import deque


def solution(prices):
    answer = []
    q = deque()
    for i in range(len(prices)):
        q.append(prices[i])

    while True:
        if len(q) == 1:
            answer.append(0)
            break
        m = min(q)
        here = q.popleft()
        if here > m:
            for i in range(len(q)):
                if here > q[i]:
                    answer.append(i + 1)
                    break
        else:
            answer.append(len(q))

    return answer

# 정확성 통과, 효율성 통과
def solution(prices):
    answer = []

    for i, p in enumerate(prices):
        time = -1
        for j in range(i, len(prices)):
            time += 1
            if p > prices[j]:
                break
        answer.append(time)

    return answer
