# 타겟넘버

def go(s, numbers, index, target):
    answer = 0
    if index == len(numbers):
        if s == target:
            return 1
        else:
            return 0
    else:
        for i in [1, -1]:
            answer += go(s + i * (numbers[index]), numbers, index + 1, target)
        return answer

def solution(numbers, target):
    answer = 0
    answer = go(0, numbers, 0, target)

    return answer