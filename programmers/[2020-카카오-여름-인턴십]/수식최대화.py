# 수식 최대화

import re
from itertools import permutations as permu


def go(order, n, expression):
    if n == len(order):
        return str(eval(expression))
    if order[n] == '*':
        temp = eval('*'.join([go(order, n + 1, new) for new in expression.split('*')]))
    elif order[n] == '-':
        temp = eval('-'.join([go(order, n + 1, new) for new in expression.split('-')]))
    elif order[n] == '+':
        temp = eval('+'.join([go(order, n + 1, new) for new in expression.split('+')]))
    return str(temp)


def solution(expression):
    answer = 0
    cal = set(re.findall('[\D]+', expression))
    order = list(permu(cal))

    for od in order:
        temp = int(go(od, 0, expression))
        answer = max(answer, abs(temp))

    return answer