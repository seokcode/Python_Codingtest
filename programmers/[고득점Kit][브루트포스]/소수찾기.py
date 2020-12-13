from itertools import permutations

def sosu(num):
    t = 2
    if num < 2:
        return False

    while t * t <= num:
        if num % t == 0:
            return False
        t += 1
    return True


def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1):
        check = list(map(''.join, permutations(numbers, i)))
        for j in list(set(check)):
            if sosu(int(j)):
                answer.append(int(j))

    answer = set(answer)
    return len(answer)

