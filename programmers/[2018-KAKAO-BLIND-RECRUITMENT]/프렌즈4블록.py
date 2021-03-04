# 프렌즈4블록

def pang(b, m, n):
    candidate = set()
    # 2X2인 블록 찾기
    # candidate에 중복되는 블록이 들어가지 않게 set.union을 이용한 합집합 연산
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] != '_':
                candidate = set.union(candidate,([(i, j), (i-1, j-1), (i-1, j), (i, j-1)]))

    # 블럭 내리기
    for i, j in candidate:
        b[i][j] = 0
    for i, row in enumerate(b):
        empty = ['_'] * row.count(0)
        b[i] = empty + [block for block in row if block != 0]
    return len(candidate)

def solution(m, n, board):
    count = 0
    b = list(map(list,zip(*board)))
    while True:
        pop = pang(b, m, n)
        if pop == 0: return count
        count += pop