# 위장

from collections import defaultdict

def solution(clothes):
    answer = 1
    d = defaultdict(list)

    for cloth, category in clothes:
        d[category].append(cloth)

    for i in d:
        answer *= (len(d[i]) + 1)

    return (answer - 1)