# 베스트앨범

from collections import defaultdict

def solution(genres, plays):
    d = defaultdict(list)
    f = defaultdict(list)
    answer = []

    for idx, genre in enumerate(genres):
        d[genre].append(plays[idx])
        f[genre + str(plays[idx])].append(idx)

    temp_d = sorted(d.items(), key=lambda x: sum(x[1]), reverse=True)

    for g, p in temp_d:
        p = sorted(p, reverse=True)
        answer.append(min(f[g + str(p[0])]))
        f[g + str(p[0])][0] = 10001
        if len(p) >= 2:
            answer.append(min(f[g + str(p[1])]))
            f[g + str(p[1])][0] = 10001

    return answer