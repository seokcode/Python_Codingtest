# 모의고사_고찰후

def solution(answers):
    answer = []
    temp = -99

    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]

    for index, num in enumerate(answers):
        if num == pattern1[index % len(pattern1)]:
            count[0] += 1
        if num == pattern2[index % len(pattern2)]:
            count[1] += 1
        if num == pattern3[index % len(pattern3)]:
            count[2] += 1

    for index, result in enumerate(count):
        if temp == -99 or temp == result:
            temp = result
            answer.append(index + 1)
        elif temp < result:
            temp = result
            answer = []
            answer.append(index + 1)

    return answer