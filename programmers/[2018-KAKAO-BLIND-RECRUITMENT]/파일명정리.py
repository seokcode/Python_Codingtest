# 파일명정리

import re


def solution(files):
    answer = []
    temp = []

    for i in files:
        temp.append(re.split('([0-9]+)', i))

    temp = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    for j in temp:
        answer.append(''.join(j))

    return answer