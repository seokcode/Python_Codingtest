# 이진변환 반복하기

import re

def go(n):
    before = len(n)
    not_zero = re.sub('[0]', '', n)
    after = len(not_zero)
    num_bin = format(len(not_zero), 'b')

    answer[0] += 1
    answer[1] += before - after
    return num_bin

def solution(s):
    global answer
    answer = [0, 0]

    num = s
    while True:
        if int(num) == 1:
            return answer
        else:
            num = go(num)