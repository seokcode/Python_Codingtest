## 답안2
def solution(n):
    counter = bin(n).count('1')

    while True:
        n += 1
        if counter == bin(n).count('1'):
            break

    return n

## 답안1
from collections import Counter


def solution(n):
    counter = Counter(format(n, 'b'))
    next = n + 1
    while True:
        compare = Counter(format(next, 'b'))
        if counter['1'] == compare['1']:
            break
        else:
            next += 1

    return next