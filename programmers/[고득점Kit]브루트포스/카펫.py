# 카펫

def solution(brown, yellow):
    y = 3
    x = 0

    while True:
        x = (yellow / (y - 2)) + 2
        x = int(x)
        if yellow == (x - 2) * (y - 2):
            if brown == (x + y - 2) * 2:
                break
        y += 1

    return [x, y]