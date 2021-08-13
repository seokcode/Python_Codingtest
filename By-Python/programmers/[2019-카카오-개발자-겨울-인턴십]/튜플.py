# 튜플

import re

def solution(s):
    answer = []
    d = dict()
    arr = re.findall('[\d+]{1,}',s)

    for i in arr:
        if i in d: d[i] += 1
        else: d[i] = 1

    answer = sorted(d.items(),key=(lambda x: x[1]),reverse=True)
    return [int(a[0]) for a in answer]