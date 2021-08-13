# 메뉴 개발

from itertools import combinations

def solution(orders, course):
    answer = []
    candidate = dict()

    for k in course:
        for i in orders:
            for j in list(combinations(i, k)):
                res = ''.join(sorted(j))
                if res in candidate:
                    candidate[res] += 1
                else:
                    candidate[res] = 1

    s_candidate = sorted(candidate, key=lambda x: candidate[x], reverse=True)

    for k in course:
        temp = 0
        for i in s_candidate:
            if len(i) == k:
                if temp == 0:
                    if candidate[i] < 2:
                        break
                    else:
                        temp = candidate[i]
                        answer.append(i)
                else:
                    if temp == candidate[i]:
                        answer.append(i)
                    else:
                        break

    answer.sort()
    return answer