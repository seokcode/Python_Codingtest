# 올바른 괄호

def solution(s):
    count = 0

    for i in s:
        if i == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False

    if count != 0:
        return False
    else:
        return True