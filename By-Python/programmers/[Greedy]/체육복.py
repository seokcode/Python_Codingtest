# 체육복

def solution(n, lost, reserve):
    lost_check = [False] * len(lost)
    reserve_check = [False] * len(reserve)
    answer = n - len(lost)

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost_check[i] = True
                reserve_check[j] = True
                answer += 1

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if not lost_check[i]:
                if not reserve_check[j]:
                    if abs(lost[i] - reserve[j]) == 1:
                        answer += 1
                        lost_check[i] = True
                        reserve_check[j] = True

    return answer