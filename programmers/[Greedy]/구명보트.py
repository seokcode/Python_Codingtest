# 구명보트

from collections import deque

def solution(people, limit):
    q = deque()
    people.sort(reverse=True)
    length = len(people)
    for i in range(length):
        q.append(people[i])
    cnt = 0

    while q:
        if q[0] <= limit // 2:
            if len(q) % 2 == 0:
                cnt += len(q) // 2
                return cnt
            else:
                cnt += (len(q) // 2) + 1
                return cnt
        else:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                cnt += 1
            else:
                q.popleft()
                cnt += 1

    return cnt