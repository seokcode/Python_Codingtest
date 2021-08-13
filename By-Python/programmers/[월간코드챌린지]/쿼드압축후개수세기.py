# 쿼드 압축 후 개수 세기

# 분할정복으로 풀자
# 분할정복은 재귀로 풀면 간단해진다

def solution(arr):
    # (0,0) (0,0+flag) (0+flag,0) (0+flag,0+flag)
    answer = [0, 0]

    def divide(x, y, n):
        flag = arr[x][y]  # 영역 내 어떤 값
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != flag:  # 모든 값이 같아야 함
                    n //= 2
                    divide(x, y, n)
                    divide(x, y + n, n)
                    divide(x + n, y, n)
                    divide(x + n, y + n, n)
                    return

        answer[flag] += 1

    divide(0, 0, len(arr))
    return answer