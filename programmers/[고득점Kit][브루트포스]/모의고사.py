# 모의고사

def solution(answers):
    answer = []
    cnt = 0
    num = 1

    while num <= 3:
        pattern = [1, 2, 3, 4, 5, 2, 1, 2, 3, 2, 4, 2, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        n = 0
        cur_cnt = 0

        if num == 1:
            pattern = pattern[:5]
            mx = 4
        elif num == 2:
            pattern = pattern[5:13]
            mx = 7
        else:
            pattern = pattern[13:]
            mx = 9

        for j in answers:
            if j == pattern[n]:
                cur_cnt += 1
            if n == mx:
                n = -1
            n += 1

        if cnt == -99 or cnt == cur_cnt:
            cnt = cur_cnt
            answer.append(num)
        elif cnt < cur_cnt:
            cnt = cur_cnt
            answer = []
            answer.append(num)

        num += 1

    if len(answer) > 1:
        answer.sort()
    return answer