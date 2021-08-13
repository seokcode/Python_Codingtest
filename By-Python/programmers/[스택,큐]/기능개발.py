# 기능 개발

from collections import deque

def solution(progresses, speeds):
    answer = []
    temp = deque([(100 - i) for i in progresses])
    sped = deque([(i) for i in speeds])

    while temp:
        cnt = 0
        for i in range(len(temp)):
            if temp[i] > 0:
                temp[i] -= sped[i]

        while temp:
            if temp[0] <= 0:
                temp.popleft()
                sped.popleft()
                cnt += 1
            else:
                break

        if cnt != 0:
            answer.append(cnt)

    return answer