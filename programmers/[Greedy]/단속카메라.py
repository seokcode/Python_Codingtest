# 단속카메라

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])

    end = -30001
    for r in routes:
        if end < r[0]:
            answer += 1
            end = r[1]

    return answer