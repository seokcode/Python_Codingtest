# 순위검색

# 정확성 통과, 효율성 실패
import re

def solution(info, query):
    info_score = []
    new_info = []
    query_score = []
    new_query = []
    answer = [0] * len(query)
    for i in query:
        query_score.append(re.findall('\d+', i))
        new_query.append(re.split(' and | [0-9]+', i))

    for i in info:
        info_score.append(re.findall('\d+', i))
        new_info.append(re.split(' | [0-9]+', i))

    n = 0
    for q in range(len(new_query)):
        for a in range(len(new_info)):
            if new_info[a][0] == new_query[q][0] or new_query[q][0] == '-':
                if new_info[a][1] == new_query[q][1] or new_query[q][1] == '-':
                    if new_info[a][2] == new_query[q][2] or new_query[q][2] == '-':
                        if new_info[a][3] == new_query[q][3] or new_query[q][3] == '-':
                            if int(query_score[q][0]) <= int(info_score[a][0]):
                                answer[n] += 1

        n += 1
    return answer

# 정확성, 효율성 다 통과
from itertools import combinations as combi
from collections import defaultdict


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in info:
        i = i.split()
        info_key = i[:-1]
        info_value = int(i[-1])
        for j in range(5):
            for c in combi(info_key, j):
                temp_key = ''.join(c)
                info_dict[temp_key].append(info_value)

    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split()
        q_value = int(q[-1])
        q = q[:-1]
        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        temp_q = ''.join(q)

        if temp_q in info_dict:
            score = info_dict[temp_q]
            n = 0
            if len(score) > 0:
                start, end = 0, len(score)
                while end > start:
                    flag = (start + end) // 2
                    if score[flag] >= q_value:
                        end = flag
                    else:
                        start = flag + 1
                answer.append(len(score) - start)
        else:
            answer.append(0)

    return answer