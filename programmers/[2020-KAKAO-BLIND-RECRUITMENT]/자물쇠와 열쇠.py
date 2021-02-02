# 자물쇠와 열쇠

# 90도 회전
def turn(arr):
    length = len(arr)
    temp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            temp[j][length - 1 - i] = arr[i][j]
    return temp


# 열쇠가 맞는지 Check
def check(x, y, key, lock, expendSize, lock_x, lock_y):
    expend = [[0] * (expendSize) for _ in range(expendSize)]

    # expend 배열에 key배열 위치 시키기
    for i in range(len(key)):
        for j in range(len(key)):
            expend[x + i][y + j] += key[i][j]

    # 열쇠 구멍이 전부 다 1인지 check
    for i in range(lock_x, lock_y + 1):
        for j in range(lock_x, lock_y + 1):
            expend[i][j] += lock[i - lock_x][j - lock_x]
            if expend[i][j] != 1:
                return False

    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)

    lock_x = M - 1  # expend에서 lock의 x인덱스 시작 지점
    lock_y = lock_x + N - 1  # expend에서 lock의 y인덱스 시작 지점

    expendSize = N + lock_x * 2

    for t in range(4):
        for i in range(lock_y + 1):
            for j in range(lock_y + 1):
                if check(i, j, key, lock, expendSize, lock_x, lock_y):
                    return True
        key = turn(key)

    return False
